import pandas as pd
import numpy as np

df = pd.read_csv(r"D:\Python_earning_roadmap\Portfolio\large_csv_clean\messy_customer_data_5k.csv")

df["customer_name"] = df["customer_name"].str.strip().str.replace(r"\s+", " ", regex = True)

df["city"] = df["city"].str.strip().str.replace(r"\s+", " ", regex = True)

df["date"] = pd.to_datetime(df["date"], format = "mixed", errors = "coerce")
df["date"] = df["date"].dt.strftime("%Y-%m-%d")

df["unit_price"] = df["unit_price"].str.replace(r"\$|,", "", regex = True).astype(float)

df = df.dropna(subset = ["state", "phone_number"])

df = df.drop_duplicates()

df.to_csv(r"D:\Python_earning_roadmap\Portfolio\large_csv_clean\spreadsheet_5k_cleaned.csv", index = False)
print(df)
