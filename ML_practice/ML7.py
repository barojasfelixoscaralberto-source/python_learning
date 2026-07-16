import pandas as pd

data = {
    "name": ["Oscar", "Ana", "Luis", "Maria", "Pedro"],
    "age": [17,21,19,25,16],
    "city": ["Culiacan", "Monterrey", "Culiacan", "CDMX", "Culiacan"]
}

df = pd.DataFrame(data)

# The first three should be easy as from numpy
print(df["age"].mean())
print(df["age"].max())
print(df["age"].min())

# Describe is like "mean, max, count" ALL OF THAT in one
# useful to check a data just sended instead of writing 1 by 1 the defs
print(df.describe())
print(round(df.describe(), 2))
