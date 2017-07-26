## Generates the circumference of a circle with a radius of 13 units and rounds to 3 places. ##

import math
radius = 13
C = round(2 * math.pi * radius, 3)
print "The circumference of a circle with a radius of 13 units is " + str(C) + " units."
