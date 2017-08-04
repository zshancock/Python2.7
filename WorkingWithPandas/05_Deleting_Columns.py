import pandas as pd
import numpy as np
from pandas import Series, DataFrame


## Dataframes: Read the Example Salary .CSV --------------------------------------------

df = pd.read_csv("C://Data//PythonFiles//MyData//Example_Salary_Data.csv")

print(df.head())

## Deleting Columns --------------------------------------------------------------------

print"------Deleting Columns-------"

del df['club']
del df['guaranteed_compensation']

print(df.head())
