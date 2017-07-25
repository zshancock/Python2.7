## Using Update Cursor, the COUNTIES shapefile's attribute table was updated to populate two existing empty fields
## NoWells (number of wells) and Density (Wells per kilometer). While running, the script prints progress for the user.


import arcpy
arcpy.env.overwriteOutput = True

# Create Wells Layer

wellsPath = "C:\\Users\\Zac\\Desktop\\Classwork\\GIS 4080\\Lesson5_Data\\Wells.shp"
arcpy.MakeFeatureLayer_management(wellsPath, "wells_lyr")

# County layer creation

countiesPath = "C:\\Users\\Zac\\Desktop\\Classwork\\GIS 4080\\Lesson5_Data\\COUNTIES.shp"
with arcpy.da.UpdateCursor(countiesPath, ['County','SHAPE_Area','NoWells','Density']) as cursor:
    for row in cursor:
        COName = row[0]
        whereClause = "County = " + "'" + str(COName)+ "'"

# Create layer with county whereClause

        arcpy.MakeFeatureLayer_management(countiesPath, "COUNTY", whereClause)

# Use selected County layer to select wells

        arcpy.SelectLayerByLocation_management("wells_lyr", "WITHIN", "COUNTY", "", "NEW_SELECTION")
        wellsCount = int(arcpy.GetCount_management("wells_lyr").getOutput(0))        

# Update No.Wells field

        row[2] = wellsCount
        cursor.updateRow(row)
        
                        
# Update wells density field ( & convert to wells per km)

        row[3] = row[2] / (row[1]/1000000)
        cursor.updateRow(row)
        
# Keep user updated when running while updating attribute table on COUNTIES.shp

        print str(COName) + ": " + str(wellsCount) + " wells."

print "NoWells and Density Fields have been updated."
