#Darryl Alexander Fleurantin
#03/28/2022
#CSC 110 Homework 6 Analysis of Algorithms ~ Part 1

#function to store the data into lists
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
 
def getData():
    inFile = openFile()  
    # Initialize the empty lists  
    yearList = []  
    awardList = []
    # Read a line from the file
    line = inFile.readline()
    # Loop while the end of file is not reached
    for line in inFile:
        # Strip the \n from the end of the line
        line = line.strip()
        # Split the items in the list separated by a comma
        year, award = line.split(",")
        # Add the year to the year list
        yearList.append(int(year))      
        # Add the award to the awards list
        awardList.append(award)              
    # Close the file
    inFile.close() 
    # Return the year list and awards list
    return yearList, awardList
 
# Function to get a valid year from user 
def getYear(yearList):
    goodYear = False
    while goodYear == False:
        try:
            year = int(input("Enter a year: "))
            if year in yearList:
                goodYear = True
            else:
                print("Year not in range, try again...")      
        except ValueError:          
            print("Invalid entry, try again ... ")
    return year

#function to search through list the binary way and computing comps
def getYearBinary(yearList, year):
    pos = 0
    comps = 0
    # left side of list    
    left = 0    
    # right side of the list                
    right = len(yearList) - 1    
    found = 0
    while right >= left and found == 0:
        comps = comps + 1
        #the middle of the list
        m = (left + right) // 2         
        if year < yearList[m]:          
            right = m - 1          
        elif year == yearList[m]:           
            found = 1
            pos = m            
        else:            
            left = m + 1
    if found == 0:   
        return -1   
    else:
        print("\nBinary Search: comps = ", comps)       
        return pos

#function to search through list the linear way and computing comps
def getYearLinear(yearList, year):
    pos = 0
    comps = 0
    found = 0
    i = 0
    while i < len(yearList) and found == 0:
        comps = comps + 1
        if yearList[i] == year:
            found = 1
            pos = i
        else:
            i = i + 1
    if found == 0:
        return -1
    else:
        print("\nLinear Search: comps = ", comps)  
        return pos

#print results
def PrintResults(pos, year, awardList):
    print("In", year,"the winner of the Tony Award for Best Musical was", awardList[pos])

#main
def main():
    yearList, awardList = getData()
    year = getYear(yearList)
    post = getYearBinary(yearList, year)
    pos = getYearLinear(yearList, year)
    PrintResults(pos, year, awardList) 
