import pandas as pd
import os

# Load raw data
df = pd.read_csv("data/raw/traffic.csv")

print("Original Shape:", df.shape)
print("Columns:", df.columns.tolist())

# Fill missing values (new way)
df = df.ffill()

# Find datetime column automatically
time_col = None

for col in df.columns:
    if "time" in col.lower() or "date" in col.lower():
        time_col = col
        break

if time_col is None:
    raise Exception("❌ No datetime column found!")

print("Using time column:", time_col)

# Convert to datetime
df[time_col] = pd.to_datetime(df[time_col])

# Extract hour
df["hour"] = df[time_col].dt.hour

# Drop old time column
df.drop(time_col, axis=1, inplace=True)

# Save clean data
os.makedirs("data/clean", exist_ok=True)

clean_path = "data/clean/traffic_clean.csv"
df.to_csv(clean_path, index=False)

print("Clean Shape:", df.shape)
print("✅ Clean data saved at:", clean_path)
