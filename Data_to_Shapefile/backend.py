# Backend for Data to Shapefile script.
# Author Zac Hancock

# -------------------------------------------------------------------------------------------
# Create a function that locates data files, and determines both what test was conducted and
# from which instrument. Write necessary information to a TEMP file.

def DataSorter(x):

    import os
    
    #Locate Data
    
    folder = "C:\\PythonPractice\\Data_to_Shapefile\\DATA"
    LabData = folder + "\\" + x + ".txt"

    if os.path.isfile(LabData):
        print "Found data file."
        print "-----"
        print "Begin Processing."
    else:
        print "Did not find data."


#Determine which instrument: SEAL AQ2, LACHAT, or Unknown
#Create an object based on the instrument (each instrument
#produces a different formatted text file for reading in
#later code).

    data = open(LabData, "r")
    output = "C:\\PythonPractice\\Data_to_Shapefile\\DATA\\TEMP.txt"
    outputFile = open(output, "w")
    
    for line in data:
        lineSegment = line.split(",")

# Write SEAL Data to a temp file, only keep what is necessary
# for a shapefile. Head document with parameter analyzed which
# will always be in segment [1] write during ICV (only once). 

        if lineSegment[1] == "SEAL AQ2 Test":
            SEALData = data
            print "Instrument Identified - SEAL AQ2"               
            for line in SEALData:
                line = line.split(",")
                if line[0] == "ICV":
                    date = line[8]
                    Date = (date.split()[0][0:2]) + "_" + (date.split()[0][3:5])
                    outputFile.write(str(line[1]) + "_" + str(Date) + "\n")
                    
                elif line[0] == "MB":
                    continue
                elif line[0] == "BS":
                    continue
                elif line[0] == "CCV":
                    continue
                elif line[0] == "CCB":
                    continue
                else:
                    outputFile.write(str(line[0]) + "," + str(line[3]) + "," + str(line[4]) + "\n")

# Write LACHAT Data to a temp file, only keep what is necessary
# for a shapefile. Head document with parameter analyzed which
# will always be in segment [5] write during ICV (only once). 

        elif lineSegment[1] == "Detection Date":
            LACHATData = data
            print "Instrument Identified - LACHAT"
            for line in LACHATData:
                line = line.split(",")
                if line[0] == "ICV":
                    date = line[1]
                    Date = (date.split()[0][0:2])+ "_" + (date.split()[0][3:5])
                    outputFile.write(str(line[5]) + "_" + str(Date) + "\n")
                    
                elif line[0] == "MB":
                    continue
                elif line[0] == "cri":
                    continue
                elif line[0] == "BS":
                    continue
                elif line[0] == "CCV":
                    continue
                elif line[0] == "CCB":
                    continue
                else:
                    outputFile.write(str(line[0]) + "," + str(line[7]) + "," + str(line[8]))
            
        else:
            print "Unknown Data format, end processing."
        break

# Close files.
    
    data.close()
    outputFile.close()
        
# -------------------------------------------------------------------------------------------          
# Create a function that updates/adds fields the Client's shapefiles based on
# DataSort TEMP file.

def WriteResults(x):

    import os
    import arcpy

# Set up workspace and open TEMP file.

    arcpy.env.overwriteOutput = True
    arcpy.env.workspace = "C:\\FinalProject\\DATA\\map"

    x = "C:\\PythonPractice\\Data_to_Shapefile\\DATA\\TEMP.txt"
    outputFile = open(x, "r")

    
# Find which test and what date - will need to name field. The first line is "Analyte_Date"
# which is perfect for the Field name (Field Name can only be 10 characters). 

    FieldName = (str(outputFile.readline()))
    field = FieldName.split()[0][0:9]
    print "Added Field '" + field + "' to the following shapefiles:" 

# Start a list for future loops.

    shapefile_list = []
    data_list = []
    a = 0

# Each client has their own shapefile. Loop through data file, and update field in each shapefile
# based on the results from each client.

    for line in outputFile:
        lineSegment = line.split(",")

# Skip the first line.

        if lineSegment[0] == FieldName:
            continue

# All other lines are client Data - update/add fields to each client's shapefile. 

        else:
            client = lineSegment[0]
            data = lineSegment[1] + " " + lineSegment[2]
            data_list.append(data)
            shapefile = "C:\\PythonPractice\\Data_to_Shapefile\\DATA\\"" + client + ".shp"
            shapefile_list.append(shapefile)
            arcpy.AddField_management(shapefile, field, "TEXT")
            print "-" + client + ".shp"
    
# Update the newly added Fields with data from the Temp File. 

    for shapefile in shapefile_list:
        
        with arcpy.da.UpdateCursor(shapefile, field) as cursor:
            for row in cursor:
                row[0] = str(data_list[a])
                cursor.updateRow(row)
        a = a + 1
    print "Next File."
    print "-----"
    print "-----"

# delete cursor and close open files.

    del cursor
    outputFile.close()

 

          
            
                
            
        
        

        

    
    

            


