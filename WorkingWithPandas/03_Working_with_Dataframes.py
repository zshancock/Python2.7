import pandas as pd
import numpy as np
from pandas import Series, DataFrame


## Dataframes: Read the Example Salary .CSV ----------------------------------------

df = pd.read_csv("C://Data//PythonFiles//MyData//Example_Salary_Data.csv")

print"-----Read the head of the .csv --------\n"

print(df.head())

print"-----Read the tail of the .csv -------- \n"

print(df.tail())

## Get the information about the dataframe -----------------------------------------

print"----Get the info about the dataframe ----\n"

print(df.info())

## Print a specific column ---------------------------------------------------------

print"----The head of the last_name column ----\n"

print(df['last_name'].head())

