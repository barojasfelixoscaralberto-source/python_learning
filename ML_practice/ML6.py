import pandas as pd

data = {
    "name": ["Oscar", "Ana", "Luis", "Maria", "Pedro"],
    "age": [17,21,19,25,16],
    "city": ["Culiacan", "Monterrey", "Culiacan", "CDMX", "Culiacan"]
}

df = pd.DataFrame(data)

# now let's use boolean masks:
# pandas just shows the already filtered objs
# BE CAREFUL, here "and" is replaced with "&"
# and the use of () and [] is a MUST

print(df[df["age"] > 18])
print(df[df["city"] == "Culiacan"])
print(df[(df["age"] > 18) & (df["city"] == "Culiacan")])