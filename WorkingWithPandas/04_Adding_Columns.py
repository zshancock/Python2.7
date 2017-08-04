import pandas as pd
import numpy as np
from pandas import Series, DataFrame


## Dataframes: Read the Example Salary .CSV --------------------------------------------

df = pd.read_csv("C://Data//PythonFiles//MyData//Example_Salary_Data.csv")

## Add a new column called "Age", there is no value set so Pandas will handle as NaN ---

print"-----Add a new column 'Age' that has no values -----\n"

print(DataFrame(df,columns=['last_name', 'first_name', 'Age']))

## Add a new columm "Double_Salary" ----------------------------------------------------

print"-----Add a new column 'Double_Salary' and populate -----\n"

df['Double_Salary'] = df['base_salary']*2

print(df.head())

## Add another column "After_Taxes" with 80% guaranteed income as populate -------------

print"-----Add a new column 'After_Taxes' and populate -----\n"

df['After_Taxes'] = df['guaranteed_compensation']*0.80

print(df.head())
