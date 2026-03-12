import pandas as pd

df = pd.read_csv("data/input.csv")

df["age_after_10_years"] = df["age"]+10

df.to_csv("data/transformed.csv", index=False)

print("Transformed job Completed")