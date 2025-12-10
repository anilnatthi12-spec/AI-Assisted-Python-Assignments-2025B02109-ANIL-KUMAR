# task3_iot_short_fixed.py
import os
import pandas as pd
import numpy as np

DEFAULT = r"D:\AI\ASSIGNMENT - 17\iot_sensor.csv"

df = pd.read_csv(DEFAULT)

print("\n--- BEFORE ---")
print(df.head())

# tolerant column names
if 'sensor_id' not in df.columns:
    df['sensor_id'] = 'sensor_0'
temp_col = next((c for c in ['temperature','temp','Temperature'] if c in df.columns), None)
hum_col  = next((c for c in ['humidity','hum','Humidity'] if c in df.columns), None)
if temp_col: df = df.rename(columns={temp_col:'temperature'})
else: df['temperature'] = np.nan
if hum_col: df = df.rename(columns={hum_col:'humidity'})
else: df['humidity'] = np.nan

# Ensure a stable index for transform (keep original order)
df = df.reset_index(drop=False).rename(columns={'index':'orig_index'})

# 1) forward fill per sensor using transform (aligned)
df['temperature'] = df.groupby('sensor_id')['temperature'].transform(lambda g: g.ffill().bfill())
df['humidity']    = df.groupby('sensor_id')['humidity'].transform(lambda g: g.ffill().bfill())

# 2) remove drift -> rolling mean (window=5) using transform (aligned)
df['temp_smooth'] = df.groupby('sensor_id')['temperature'].transform(
    lambda g: g.rolling(window=5, min_periods=1).mean()
)
df['hum_smooth']  = df.groupby('sensor_id')['humidity'].transform(
    lambda g: g.rolling(window=5, min_periods=1).mean()
)

# 3) standard scaling per sensor (manual) using group-level mean/std via transform
eps = 1e-9
temp_mean = df.groupby('sensor_id')['temp_smooth'].transform('mean')
temp_std  = df.groupby('sensor_id')['temp_smooth'].transform(lambda x: x.std(ddof=0)).replace(0, eps)
df['temp_scaled'] = (df['temp_smooth'] - temp_mean) / temp_std

hum_mean = df.groupby('sensor_id')['hum_smooth'].transform('mean')
hum_std  = df.groupby('sensor_id')['hum_smooth'].transform(lambda x: x.std(ddof=0)).replace(0, eps)
df['hum_scaled'] = (df['hum_smooth'] - hum_mean) / hum_std

# 4) encode sensor id (fast)
df['sensor_encoded'] = pd.factorize(df['sensor_id'].astype(str))[0]

# restore original index order (if needed)
df = df.sort_values('orig_index').drop(columns=['orig_index']).reset_index(drop=True)

print("\n--- AFTER ---")
print(df[['sensor_id','temperature','temp_smooth','temp_scaled','sensor_encoded']].head())

# Same quick checks as your screenshot
assert df['temperature'].isna().sum() == 0, "temperature still has NaNs"
assert 'temp_scaled' in df.columns, "temp_scaled missing"
assert df['sensor_encoded'].nunique() > 0, "sensor_encoded not created"

print("\nTask 3 Passed All Tests ✓")
