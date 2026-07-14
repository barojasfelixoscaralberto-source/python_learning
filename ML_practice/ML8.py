import pandas as pd

data = {
    "name": ["Oscar", "Lissandro", "Angy", "Santiago", "Javivi"],
    "age": [17, 18, 18, 18, 19],
    "city": ["Culiacan", "CDMX", "Culiacan", "Guasave", "Japon"]
}

df = pd.DataFrame(data)
# To add a column
df["score"] = [85, 92, 78, 95, 70]

# to erase a column "drop"
df = df.drop(columns=["score"])
print(df)


