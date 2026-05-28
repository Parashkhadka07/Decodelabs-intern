import pandas as pd 
import seaborn as sns

#  for the loading dataframe from the seaborn

df=sns.load_dataset("titanic")
print("database loaded sucessfully")


# checking missing values

print("="*50)
print("missing values")
print("="*50)

print(df.isnull().sum())

print("="*50)


# ── STEP 3: Handle Missing Values ────────────────────────────
print("=" * 50)
print("🔧 FIXING MISSING VALUES")
print("=" * 50)

#  age is filled with the median
df['age']=df["age"].fillna(df["age"].median())
print(f"empty values are filled with {df['age'].median()}")

#  embarked is filled with the mode
df["embarked"]=df["embarked"].fillna(df["embarked"].mode()[0])
print(f"empty values are filed with {df['embarked'].mode()[0]}")

# 'embark_town' → fill with most common town
df['embark_town'] = df['embark_town'].fillna(df['embark_town'].mode()[0])
print(f"✅ 'embark_town' filled with mode {df['embark_town'].mode()[0]}")

# 'deck' → too many missing (77%), drop the column
df = df.drop(columns=['deck'])
print("✅ 'deck' column dropped (77% missing)")
print()


# ── STEP 4: Remove Duplicates ─────────────────────────────────
print("=" * 50)
print("🗑️  REMOVING DUPLICATES")
print("=" * 50)
before = len(df)
df = df.drop_duplicates()
after = len(df)
print(f"Rows before : {before}")
print(f"Rows after  : {after}")
print(f"Duplicates removed : {before - after}")
print()

# ── STEP 5: Fix Data Types ────────────────────────────────────
print("=" * 50)
print("🔄 FIXING DATA TYPES")
print("=" * 50)

# 'survived' and 'pclass' should be category, not int
df['survived'] = df['survived'].astype('category')
df['pclass']   = df['pclass'].astype('category')
df['sex']      = df['sex'].astype('category')
df['embarked'] = df['embarked'].astype('category')

print("✅ Converted survived, pclass, sex, embarked → category")
print()

# ── STEP 6: Rename columns for clarity ───────────────────────
print("=" * 50)
print("✏️  RENAMING COLUMNS")
print("=" * 50)
df = df.rename(columns={
    'survived'  : 'Survived',
    'pclass'    : 'Passenger_Class',
    'sex'       : 'Gender',
    'age'       : 'Age',
    'fare'      : 'Fare',
    'embarked'  : 'Embarked'
})
print("✅ Key columns renamed for clarity")
print(df)

# ── STEP 7: Check missing values AFTER cleaning ──────────────
print("=" * 50)
print("✅ MISSING VALUES (AFTER)")
print("=" * 50)
print(df.isnull().sum())
print()


# ── STEP 8: Final clean dataset preview ──────────────────────
print("=" * 50)
print("👀 CLEANED DATASET (first 5 rows)")
print("=" * 50)
print(df.head())
print()

print("=" * 50)
print(f"✅ Cleaning complete! Final shape: {df.shape}")
print("=" * 50)
