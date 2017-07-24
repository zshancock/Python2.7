## Use cities shapefile to generate a text file that includes CityName, CoordX,## and CoordY on a single line.
## Could be used for any shapefile assuming the paths are updated in fClass and output.

import arcpy

# Define paths/files.

fClass = "C:\\Users\\Zac\\Desktop\\Classwork\\GIS 4080\\Lesson6_Data\\Cities.shp"
output = "C:\\Users\\Zac\\Desktop\\Classwork\\GIS 4080\\Lesson6_Data\\Coordinates.txt"

# Open destination file with WRITE mode.

outputFile = open(output, "w")

# Write headings on output file a single time (i.e. not looped).

outputFile.write("City Name" + ", " + "CoordinateX" + ", " + "CoordinateY" + "\n")

# Use cursor to find City Name, X, Y. WRITE this to new text file. 

cursor = arcpy.da.SearchCursor(fClass, ["NAME","SHAPE@X","SHAPE@Y"]
for row in cursor:    
  outputFile.write(str(row[0]) + ", " + str(row[1]) + ", " + str(row[2]) + "\n")    
  #print str(row[0]) + ", " + str(row[1]) + ", " + str(row[2]) + "\n"

# Close file.
outputFile.close()
