import pandas as pd
import numpy as np
from pandas import Series, DataFrame

## Getting fimiliar with Series in Pandas ------------------------------------------

this = Series([6,5,4,9,2])

print this         # Series
print this.values  # Series output in array format
print this.index   # the index automatically generated from Pandas

print "--------------------"

## Making a Series with an Index ---------------------------------------------------

citypopulation_2016 = Series([8537673,3976322,2704958,2303482,1615017],
                             index=['NYC','Los Angeles','Chicago','Houston',
                                    'Phoenix'])
print citypopulation_2016

print "-------------------"

## Find Population lesser than 2.5 million -----------------------------------------

print citypopulation_2016[citypopulation_2016<2500000]
