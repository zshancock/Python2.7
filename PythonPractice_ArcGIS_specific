## Find all cities in the Colorado set and return only those in Jefferson County: return the names
## of the cities and print the number of cities in selection. Could be used with any Colorado county
## assuming the shapefile was used in place of the JeffCOLayer. 


import arcpy

citiesPath = "C:\\Users\\Zac\\Desktop\\Classwork\\GIS 4080\\Lesson5_Data\\Colorado_cities.shp"
JeffCOLayer = "C:\\Users\\Zac\\Desktop\\Classwork\\GIS 4080\\Lesson5_Data\\Jefferson.shp"

arcpy.MakeFeatureLayer_management(citiesPath, "cities_lyr")
arcpy.SelectLayerByLocation_management("cities_lyr", "INTERSECT", JeffCOLayer, "", "NEW_SELECTION")

fieldList = "name"
with arcpy.da.SearchCursor("cities_lyr", fieldList) as cursor:
    for row in cursor: print row[0]

citiesCount = int(arcpy.GetCount_management("cities_lyr").getOutput(0))
print "There are " + str(citiesCount) + " cities in this selection."
