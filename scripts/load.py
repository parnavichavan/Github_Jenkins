import pandas as pd
import sqlite3

df = pd.read_csv("data/transformed.csv")

conn = sqlite3.connect("data/users.db")

df.to_sql("users", conn, if_exists="replace", index=False)

print("Load job completed")