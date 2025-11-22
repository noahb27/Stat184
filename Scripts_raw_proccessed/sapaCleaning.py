import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# === 1. LOAD DATA ===
file_path = r"C:\Users\socce\OneDrive\Desktop\personality-major-mvp\Raw_data\sapaTempData696items08dec2013thru26jul2014.tab"
df = pd.read_csv(file_path, sep="\t", low_memory=False)

print("Original shape:", df.shape)


# === 2. IDENTIFY NUMERIC PERSONALITY ITEMS ===
# SAPA items are numeric; demographics are strings

numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
print("Numeric columns:", len(numeric_cols))

# Remove known demographic numeric fields if they exist
demographics = ["age", "education", "engnat", "gender", "race", "country"]
item_cols = [c for c in numeric_cols if not any(d in c.lower() for d in demographics)]

print("Detected personality items:", len(item_cols))


# === 3. IMPUTE MISSING VALUES ===
df[item_cols] = df[item_cols].apply(lambda col: col.fillna(col.mean()))


# === 4. STANDARDIZE PERSONALITY ITEMS ===
scaler = StandardScaler()
scaled = scaler.fit_transform(df[item_cols])
df_scaled = pd.DataFrame(scaled, columns=item_cols)

print("Scaled personality matrix shape:", df_scaled.shape)


# === 5. SAVE OUTPUT ===
df_scaled.to_csv(r"C:\Users\socce\OneDrive\Desktop\personality-major-mvp\Processed\sapa_personality_scaled.csv", index=False)
df.to_csv(r"C:\Users\socce\OneDrive\Desktop\personality-major-mvp\Processed\sapa_clean_full.csv", index=False)

print("Saved cleaned SAPA files successfully!")
