# task2_financial_short.py
import pandas as pd
import numpy as np
from dateutil import parser as dateparser

DEFAULT = r"D:\AI\ASSIGNMENT - 17\financial_data.csv"

df = pd.read_csv(DEFAULT)

print("\n==================  TASK 2: FINANCIAL DATA  ==================\n")
print("\n--- BEFORE ---\n")
print(df.head())

# Normalize column names tolerance
if 'closing_price' not in df.columns:
    price_col = next((c for c in ['close','Close','closing'] if c in df.columns), None)
    if price_col: df = df.rename(columns={price_col: 'closing_price'})

if 'volume' not in df.columns:
    vol_col = next((c for c in ['Volume','vol','trade_volume'] if c in df.columns), None)
    if vol_col: df = df.rename(columns={vol_col: 'volume'})

# 1) Handle missing values
df['closing_price'] = pd.to_numeric(df.get('closing_price'), errors='coerce')
df['closing_price'] = df['closing_price'].ffill().bfill()

df['volume'] = pd.to_numeric(df.get('volume'), errors='coerce')
df['volume'] = df['volume'].fillna(int(df['volume'].median(skipna=True) if not np.isnan(df['volume'].median(skipna=True)) else 0)).astype(int)

# 2) Lag features: returns
df['return_1d'] = df['closing_price'].pct_change(periods=1)
df['return_7d'] = df['closing_price'].pct_change(periods=7)

# 3) Log-scale volume
df['volume_log'] = np.log1p(df['volume'])

# 4) Outlier detection (IQR) on closing_price and remove outliers
q1 = df['closing_price'].quantile(0.25)
q3 = df['closing_price'].quantile(0.75)
iqr = q3 - q1
lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr
df = df[(df['closing_price'] >= lower) & (df['closing_price'] <= upper)].reset_index(drop=True)

print("\n--- AFTER ---\n")
# show date if exists, else show head with key cols
cols_show = []
if 'date' in df.columns:
    cols_show.append('date')
cols_show += [c for c in ['closing_price','volume','return_1d','return_7d','volume_log'] if c in df.columns]
print(df[cols_show].head())

# Simple tests (same style as your reference)
assert df['volume'].isna().sum() == 0, "volume has NaNs"
assert 'return_1d' in df.columns, "return_1d missing"
assert df['volume_log'].min() >= 0, "volume_log negative"

print("\nTask 2 Passed All Tests ✓\n")
