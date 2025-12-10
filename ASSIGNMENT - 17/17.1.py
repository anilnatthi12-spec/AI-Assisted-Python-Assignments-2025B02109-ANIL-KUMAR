# task1_social_short.py
import re
import os
import pandas as pd
import numpy as np
DEFAULT = r"D:\AI\ASSIGNMENT - 17\social_media.csv"
df = pd.read_csv(DEFAULT)
print("\n--- BEFORE ---")
print(df.head())
# tolerant column names
text_col = next((c for c in ['post_text','text','content','post'] if c in df.columns), None)
if text_col is None:
    # fallback to first object column
    text_col = next((c for c in df.columns if df[c].dtype == object), df.columns[0])
# simple stopwords list (small, avoids nltk)
STOPWORDS = {
 'a','an','the','and','or','is','it','this','that','in','on','for','to','of','with','as','at','by'
}
# normalization: lowercase, remove urls, punctuation, special chars, remove stopwords
url_re = re.compile(r'https?://\S+|www\.\S+')
punct_re = re.compile(r'[^0-9a-z\s#@]')   # keep hashtags and mentions if needed
def clean(t):
    if pd.isna(t):
        return ''
    s = str(t).lower()
    s = url_re.sub(' ', s)
    s = punct_re.sub(' ', s)
    tokens = [w for w in s.split() if w not in STOPWORDS]
    return ' '.join(tokens).strip()

df['clean_post'] = df[text_col].apply(clean)
# handle missing likes/shares
df['likes'] = pd.to_numeric(df.get('likes'), errors='coerce').fillna(0).astype(int)
df['shares'] = pd.to_numeric(df.get('shares'), errors='coerce').fillna(0).astype(int)
# timestamp -> datetime, hour, weekday (if timestamp column exists)
ts_col = next((c for c in ['timestamp','time','created_at','date'] if c in df.columns), None)
if ts_col:
    df['timestamp'] = pd.to_datetime(df[ts_col], errors='coerce')
else:
    df['timestamp'] = pd.NaT
df['hour'] = df['timestamp'].dt.hour
df['weekday'] = df['timestamp'].dt.day_name()
# spam heuristics: empty, too short, many hashtags, has url in original text
def is_spam_row(row):
    txt = str(row.get(text_col,''))
    c = row['clean_post']
    if not c or len(c.split()) < 2:
        return True
    if txt.count('#') > 5:
        return True
    if re.search(url_re, txt):
        return True
    return False
df['_is_spam'] = df.apply(is_spam_row, axis=1)
# remove duplicates by clean_post and spam
df = df[~df['_is_spam']].copy()
df = df.drop_duplicates(subset=['clean_post'], keep='first').reset_index(drop=True)

print("\n--- AFTER CLEANING ---")
print(df[[text_col,'clean_post','likes','shares','hour']].head())

# simple tests like your examples
assert df['clean_post'].isna().sum() == 0, "clean_post has NaNs"
assert df['likes'].isna().sum() == 0, "likes has NaNs"
assert 'hour' in df.columns, "hour column missing"

print("\nTask 1 Passed All Tests ✓")
