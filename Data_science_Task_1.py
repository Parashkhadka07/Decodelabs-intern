import pandas as pd
import seaborn as sns
# load the dataset
df=sns.load_dataset('titanic')
print("Dataset loaded Sucessfully")

#  this is for the dataset size and ahape
print("="*50)
print("Dataset size")
print("="*50)
rows,colm=df.shape
print(f"rows:{rows}")
print(f"colm:{colm}")

print("=" * 50)
print("📋 COLUMNS AND DATA TYPES")
print("=" * 50)
print(df.dtypes)
print()

# ── STEP 4: First 5 Rows ─────────────────────────────────────
print("=" * 50)
print("👀 FIRST 5 ROWS (Sample Data)")
print("=" * 50)
print(df.head())
print()

# ── STEP 5: Dataset Info ─────────────────────────────────────
print("=" * 50)
print("ℹ️  DATASET INFO")
print("=" * 50)
df.info()
print()

# ── STEP 6: Basic Statistics ─────────────────────────────────
print("=" * 50)
print("📊 BASIC STATISTICS")
print("=" * 50)
print(df.describe())
print()


# ── STEP 7: Missing Values ───────────────────────────────────
print("=" * 50)
print("❓ MISSING VALUES PER COLUMN")
print("=" * 50)
print(df.isnull().sum())
print()

# ── STEP 8: What This Dataset Represents ────────────────────
print("=" * 50)
print("📌 ABOUT THIS DATASET")
print("=" * 50)
print("""
The Titanic dataset contains information about passengers
aboard the RMS Titanic, which sank on April 15, 1912.

Key columns:
- survived  : Whether the passenger survived (0 = No, 1 = Yes)
- pclass    : Ticket class (1 = 1st, 2 = 2nd, 3 = 3rd)
- sex       : Gender of the passenger
- age       : Age in years
- fare      : Ticket fare paid
- embarked  : Port of embarkation (C, Q, or S)

Total passengers : 891
Total features   : 15
""") 
