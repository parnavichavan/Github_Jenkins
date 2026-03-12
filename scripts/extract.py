import pandas as pd
import os

os.makedirs("data", exist_ok=True)

data= {
    "name": ["sai","pran","sam"],
    "age": [25,29,25]
}

df =pd.DataFrame(data)
df.to_csv("data/input.csv", index= False)
print("Extract job completed")