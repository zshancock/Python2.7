## Generates the circumference of a circle with a radius variable (can be changed) units and rounds to 3 places. ##

import math
radius = 13  # can be changed
C = round(2 * math.pi * radius, 3)
print "The circumference of a circle with a radius of " + str(radius) + " units is " + str(C) + " units."
