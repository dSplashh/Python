
#Darryl Alexander Fleurantin
#03/21/2022
#CSC 110 Homework 5 Working with Files ~ Part 1

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
 
# Function to get a valid year from user
def getYear():
    goodInput = False
    while goodInput == False:
        try:
            year = int(input("Enter a year between 1895 and 2016: "))
            if year <= 2016 and year >= 1895:
                goodInput = True
            else:
                print("Year not in range, try again...")    
        except ValueError:       
            print("Invalid entry, try again ... ")
    return year

#function to get the count of shadows in the 5 year span from given year
def shadowTrend(year, yearList, shadowList):
    count = 0
    yearPlus = year + 5
    yearLess = year - 5
    if yearPlus > 2016 or yearLess < 1895: 
        return -1
    else:
        index = yearList.index(year)
        for i in range(5):    
            if shadowList[index + i] == "Full Shadow":          
                count = count + 1           
        percent = (count/5)*100
    return percent

#prints results
def printResults(percent, year):
    if percent == -1:
        print("Five year trend cannot be computed from the given year", year)
    else:
        print("Phil saw his shadow ", percent, " % of the five years starting in ", year)

#main
def main():
    yearList, shadowList, diffList = getData()
    year = getYear()
    percent = shadowTrend(year, yearList, shadowList)
    printResults(percent, year)
