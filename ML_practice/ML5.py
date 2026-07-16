import pandas as pd

data = {
"name": ["Oscar", "Ana", "Luis"],
"age": [17,21,19],
"city": ["Culiacan", "Monterrey", "CDMX"]
}

# Just a reminder: 
# [] 1D serie
# [[]] 2D DataFrame

df = pd.DataFrame(data)
print(df["name"]) # Prints all the names but as serie
print(df[["name", "age"]]) # prints all the names & ages but as a dataframe
print(df.loc[0]) # locates row 0
print(df.loc[1:2]) #locates row 1 to 2 (here un 2D we include the last digit provided)
