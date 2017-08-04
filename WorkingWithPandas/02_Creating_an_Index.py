import pandas as pd
import numpy as np
from pandas import Series, DataFrame


citypopulation_2016 = Series([8537673,3976322,2704958,2303482,1615017],
                             index=['NYC','Los Angeles','Chicago','Houston',
                                    'Phoenix'])

## Create a list of Index ----------------------------------------------------------

print " ------Creating an Index as an object------"

cities = ['NYC','Los Angeles','Chicago','Houston','Phoenix','Philadelphia']

Ser = Series(citypopulation_2016, index=cities)

print Ser

print "--------Adding two Series for a new object--"

## Adding two Series to create a new object ----------------------------------------

Ser1 = Ser + citypopulation_2016

print Ser1

## Name the Index (Label) ----------------------------------------------------------

print "-----Name the Index---------------------"

Ser1.index.name = 'Cities'

print Ser1
