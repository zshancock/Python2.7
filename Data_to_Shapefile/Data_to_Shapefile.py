

from backend import *

if __name__ == '__main__':

# Gather a single file or a list of files ------------------------------------- 
    
    LabData_list = []
    print "List the data files (one at a time) to process, enter a space to quit."
    while True:
        data = raw_input("LabData File: ")
        if data == " ":
            break
        else:
            LabData_list.append(data)


# Process list with custom tools -----------------------------------------------

    index = 0
    
    for files in LabData_list:

        complete = DataSorter(LabData_list[index])
        complete = WriteResults("C:\\PythonPractice\\Data_to_Shapefile\\DATA\\TEMP.txt")
        index = index + 1

    print "No more files found."
    print "-----"
    print "-----"
    print "Done Processing Lab Data."
