## Zac Hancock: Working with Rasters. Take Rivers, Lakes, RockPorosity and LandUsage Rasters     ##
## and reclassify. Then with reclassified rasters, perform map algebra to generate a new raster  ##
## that multiplies all rasters to generate areas at the Highest Risk of water pollution.         ##

import arcpy

# set up environments & check out spatial analyst extension -------------------------

arcpy.env.overwriteOutput = Truearcpy.env.workspace = "C:\\Users\\Zac\\Desktop\\Classwork\\GIS 4080\\Lesson_7_Data"
arcpy.CheckOutExtension("Spatial")
print "Begin processing."

# Begin reclassifying the Rivers,Lakes and RockPor rasters --------------------------

# Define Reclass Rules(NOTE: Land Use requires no reclassification and is ready for map algebra in current state).

Field = "VALUE"
riverList = []
riverList.append([1,0])
riverList.append(["NoData",1])
RiverRemap = arcpy.sa.RemapValue(riverList)

lakeList = []lakeList.append([1,0])
lakeList.append(["NoData",1])
LakeRemap = arcpy.sa.RemapValue(lakeList)

rockList = []
rockList.append([1,3,1])
rockList.append([3,6,2])
rockList.append([6,9,3])
rockList.append([9,12,4])
rockList.append([12,15,5])
rockRemap = arcpy.sa.RemapRange(rockList)

# Generate Reclassify Rasters 

RE_river = arcpy.sa.Reclassify("reclassriv", Field, RiverRemap, "NODATA")
RE_river.save("C:\\Users\\Zac\\Desktop\\Classwork\\GIS 4080\\Lesson_7_Data\\RE_river")
print "-> River Raster reclassified."

RE_lake = arcpy.sa.Reclassify("lakebuff", Field, LakeRemap, "NODATA")
RE_lake.save("C:\\Users\\Zac\\Desktop\\Classwork\\GIS 4080\\Lesson_7_Data\\RE_lake")
print "-> Lakes Raster reclassified."

RE_rockpor = arcpy.sa.Reclassify("rockPor", Field, rockRemap, "NODATA")
RE_rockpor.save("C:\\Users\\Zac\\Desktop\\Classwork\\GIS 4080\\Lesson_7_Data\\RE_rockpor")
print "-> Rock Porosity reclassified."

# Use Map Algebra to identify the highest risk of water pollution. ------------------

Landusep = "C:\\Users\\Zac\\Desktop\\Classwork\\GIS 4080\\Lesson_7_Data\\Landusep"
WaterRisk = RE_river * RE_lake * Landusep * RE_rockpor
WaterRisk.save("C:\\Users\\Zac\\Desktop\\Classwork\\GIS 4080\\Lesson_7_Data\\WaterRisk")
print "--> Map Algebra conducted, WaterRisk raster created."

# Clip WaterRisk to correctly represent area of interest. ---------------------------

ClipExtent = "C:\\Users\\Zac\\Desktop\\Classwork\\GIS 4080\\Lesson_7_Data\\ColoradoAreaOfInterest.shp"
Risk_Clip = "C:\\Users\\Zac\\Desktop\\Classwork\\GIS 4080\\Lesson_7_Data\\Risk_Clip"
FinalClip = arcpy.Clip_management("WaterRisk","#", Risk_Clip, ClipExtent, "0", "ClippingGeometry")
print "----> WaterRisk clipped to appropriate area, Final raster created."

# Check in spatial analyst extension. -----------------------------------------------

arcpy.CheckInExtension("Spatial")
print "End processing."
