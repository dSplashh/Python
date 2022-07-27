
#Darryl Alexander Fleurantin
#03/21/2022
#CSC 110 Homework 5 Working with Files ~ Part 2

#function to open and read file
def openFile():   
    goodFile = False 
    while goodFile == False:    
        fname = input("Please enter the name of the data file: ")       
        # Begin exception handling     
        try:         
            # Try to open the file using the name given           
            inFile = open(fname, 'r')          
            # If the name is valid, set Boolean to true to exit loop          
            goodFile = True          
        except IOError:          
            # If the name is not valid - IOError exception is raised          
            print("Invalid file name, try again ... ")         
    return inFile

#function to store the data into lists
def getData():
    inFile = openFile()   
    # Initialize the empty lists    
    yearList = []  
    shadowList = []  
    diffList = []
    # Read a line from the file 
    line = inFile.readline()
    # Loop while the end of file is not reached
    for line in inFile:
        # Strip the \n from the end of the line
        line = line.strip()
        # Split the items in the list separated by a comma
        year, shadowInfo, febaveTemp, marchaveTemp, diffTemp = line.split(",")
        # Add the year to the year list
        yearList.append(int(year))  
        # Add the shadow data to the shadow list
        shadowList.append(shadowInfo)
        # Add the difference from the averages to a list
        diffList.append(float(diffTemp))                  
    # Close the file
    inFile.close()
    # Return the year list, shadow list, and difference list
    return yearList, shadowList, diffList

def thres():
    goodInput = False
    while goodInput == False:
        try:
            diffThreshold = float(input("Enter a threshold for temperature difference: "))
            goodInput = True
        except ValueError:
            print("Invalid entry, try again...")
    return diffThreshold

def tempDiffFile(diffThreshold, yearList, shadowList, diffList):   
    outName = "shadow" + str(diffThreshold) + ".csv"
    outFile = open(outName, 'w')
    outFile.write("year" + "," + "shadow" + "," + "temperature difference" + '\n')
    for i in range(len(diffList)):
        if diffList[i] >= diffThreshold:
            outFile.write(str(yearList[i]) + "," + shadowList[i] + "," + str(diffList[i]) + '\n')
    outFile.close()
    return

def printResults(diffThreshold):
    outName = "shadow" + str(diffThreshold)
    print("The results have been written to the output file:", outName + ".csv")
    
#main
def main():
    yearList, shadowList, diffList = getData()
    diffThreshold = thres()
    tempDiffFile(diffThreshold, yearList, shadowList, diffList)
    printResults(diffThreshold) 
