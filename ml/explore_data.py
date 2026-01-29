import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/traffic.csv")

print("===== BASIC INFO =====")
print("Shape (rows, columns):", df.shape)

print("\n===== COLUMN NAMES =====")
print(df.columns)

print("\n===== FIRST 5 ROWS =====")
print(df.head())

print("\n===== DATA TYPES =====")
print(df.dtypes)

print("\n===== MISSING VALUES =====")
print(df.isnull().sum())
