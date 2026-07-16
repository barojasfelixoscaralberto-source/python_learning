'''
Sobre el mismo dataframe, agrega una columna status que diga approved o failed
segun si el grade es mayor o igual a 70. 
usa np.where(if, value true, value false)
'''
import numpy as np
from Exercise4ML import df

print(df)
df["status"] = np.where(df["grade"] >= 70, "approved", "failed")
print(df)