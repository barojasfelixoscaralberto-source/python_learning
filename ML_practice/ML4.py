import pandas as pd

data = {
"name": ["Oscar", "Ana", "Luis"],
"age": [17,21,19],
"city": ["Culiacan", "Monterrey", "CDMX"]
}

df = pd.DataFrame(data)
print(df) # pandas works as Excel, tabs everything using diccionaries
# pandas uses the same format (row, column)

print(df.shape) # shows the actual range of the table (3, 3)
print(df.columns) # shows the columns that we have
print(df.dtypes) # shows the data types of the columns (str, int, bool, obj, float)
print(df.head(2)) # shows the n rows that we asked for (default's 5)