#Darryl Alexander Fleurantin
#04/1/2022
#CSC 110 Final Project ~ Movie Information

#function to open file
#tests if file is a valid file
#returns the contents of the file
def openFile():
    goodFile = False
    while goodFile == False:        
        fname = input("Please enter a file name: ")        
        # Begin exception handling        
        try:            
            # Try to open the file using the name given            
            inFile = open(fname, 'r')            
            # If the name is valid, set Boolean to true to exit loop            
            goodFile = True
        except IOError:
            # If the name is not valid - IOError exception is raised
            print("Invalid file name try again ... ")
    return inFile

#function to get the data
#store the data in a list
#returns lists of data
def getData():
    inFile = openFile()    
    #Initialize the empty lists
    titleList = []    
    genreList = []
    directorList = []
    yearList = []
    runtimeList = []
    revenueList = [] 
    # Read a line from the file
    line = inFile.readline()
    # Loop while the end of file is not reached
    for line in inFile:
        # Strip the \n from the end of the line
        line = line.strip()
        #Split the items in the list separated by a comma
        title, genre, director, year, runtime, revenue = line.split(",")
        #Add the title to the title list
        titleList.append(title)
        #Add the genre to the genre list
        genreList.append(genre)
        #Add the director to the director list
        directorList.append(director)
        #Add the year to the year list
        yearList.append(int(year))
        #Add the run time to the run time list
        runtimeList.append(int(runtime))
        #Add the revenue to the revenue list
        revenueList.append(float(revenue))    
    # Close the file
    inFile.close()
    # Return the title list, genre list, director list, year list, run time list, and revenue list
    return titleList, genreList, directorList, yearList, runtimeList, revenueList

#CHOICE 1 ~ Find all films made by a specified director ----------------------------------
#-----------------------------------------------------------------------------------------

#function to get a valid director
#takes the parameter of the director list
def validName(directorList):
    #loops through director list checking if the user input name is in directorList
    #returns the name if this statement^ is true
    #if false it prints invalid entry - try again and will loop again asking for name until true
    while True:
        name = input("Enter director: ")
        for director in directorList:
            if name == director:
                return name
        print("Invalid entry - Try again")

#function to get the index of the returned name in director list
#takes the parameters of the director list and the returned name
def directorIndex(directorList, name):
    #Initialize the empty list for director index
    directIndex = []
    #loops through director list checking if directorList at position i equals name
    #appends positions i in director index if this statement^ is true
    for i in range(len(directorList)):
        if name == directorList[i]:
            directIndex.append(i)
    #return director index
    return directIndex

#function for printing film search results
#takes parameters of director index, title list, genre list, director list, year list, runtime list, revenue list
def printfilmSearch(directIndex, titleList, genreList, directorList, yearList, runtimeList, revenueList):
    print("\nThe films that meet your criteria are:\n")
    print("TITLE".ljust(45), "GENRE".ljust(35), "DIRECTOR".ljust(24), "YEAR".ljust(8), "RUNTIME".ljust(8), "REVENUE(mil)".rjust(12))
    for i in directIndex:
        print(titleList[i].ljust(45), genreList[i].ljust(35), directorList[i].ljust(24), str(yearList[i]).ljust(8), str(runtimeList[i]).ljust(8), ("$"+str(revenueList[i])).rjust(12))
        
#CHOICE 1 ~ -------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------

#CHOICE 2 ~ Find the highest grossing film made in a specific year -----------------------------------------
#-----------------------------------------------------------------------------------------------------------

#function to get a valid year      
def getYear():
    #initialize good input as false
    goodInput = False
    #loop for handling user input if not an integer or not in range
    while goodInput == False:
        try:
            year = int(input("Enter year: "))
            if year >= 2006 and year <= 2016:
                goodInput = True
            else:
                print("Year out of range, must be between 2006 and 2016")     
        except ValueError:
            print("Invalid entry - Try again")
    #returns year
    return year

#function to get every of the returned year index
#takes the parameters of the returned year and the year list
def allYearIndex(year, yearList):
    #initialize the empty year index list
    yearIndex = []
    #loop for appending index i if the returned year equals year list at position i 
    for i in range(len(yearList)):
        if year == yearList[i]:
            yearIndex.append(i)
    #return year index
    return yearIndex

#function to get the highest grossing film index
#takes the parameters of the returned year index and the revenue list
def highGrossIndex(yearIndex, revenueList):
    #initialize the empty revenue index list
    revIndex = []
    #initialize high gross variable as revenue list at position 0
    highGross = revenueList[0]
    #loop for checking highest gross at the position of every of the returned year index
    #sets high gross variable as revenue list at position i if revenue list at position is greater than high gross
    for i in yearIndex:
        if revenueList[i] > highGross:
            highGross = revenueList[i]
    #loop for getting index of high gross
    #loops through revenue list at position j
    #if high gross equals revenue list at position j append j in revenue index
    for j in range(len(revenueList)):
        if highGross == revenueList[j]:
            revIndex.append(j)
    #return revenue index
    return revIndex

#function for printing highest grossing film results
#takes parameters of revenue index, title list, genre list, director list, year list, runtime list, revenue list
def printhighGrossFilm(revIndex, titleList, genreList, directorList, yearList, runtimeList, revenueList):
    results = []
    print("\nThe film that meets your criteria is:\n")
    print("TITLE".ljust(45), "GENRE".ljust(35), "DIRECTOR".ljust(24), "YEAR".ljust(8), "RUNTIME".ljust(8), "REVENUE(mil)".rjust(12))
    for i in revIndex:
        print(titleList[i].ljust(45), genreList[i].ljust(35), directorList[i].ljust(24), str(yearList[i]).ljust(8), str(runtimeList[i]).ljust(8), ("$"+str(revenueList[i])).rjust(12))
        
#CHOICE 2 ~ -------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

#CHOICE 3 ~ Find all films made in a given year range in a specified genre -------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------

#function to get a valid first year  
def getYear1():
    #initialize good input as false
    goodInput = False
    #loop for handling user input if not an integer or not in range
    while goodInput == False:
        try:
            year1 = int(input("Year1: "))
            if year1 >= 2006 and year1 <= 2016:
                goodInput = True
            else:
                print("Year out of range, must be between 2006 and 2016")     
        except ValueError:
            print("Invalid entry - Try again")
    #return year 1
    return year1

#function for getting second year
#takes the parameter of year 1
def getYear2(year1):
    #initialize good input as false
    goodInput = False
    #loop for handling user input if not an integer or not in range or not greater than year 1
    while goodInput == False:
        try:
            year2 = int(input("Year2: "))
            if year2 >= 2006 and year2 <= 2016:
                if year2 > year1:
                    goodInput = True
                else:
                    print("Second year should be after first year - try again")
                    year1 = getYear1()
            else:
                print("Year out of range, must be between 2006 and 2016")   
        except ValueError:
            print("Invalid entry - Try again")
    #return year 2
    return year2

#function for getting the index of every year between the returned year 1 and year 2
#takes the parameters of year 1, year 2, and the year list
def yearGenreSearchIndex(year1, year2, yearList):
    #initialize the empty index list between the returned year 1 and year 2
    yearGenreIndex = []
    #loop for appending the index of year 1 if year 1 equals year list at position index up until it reaches year 2
    while year1 < year2 + 1:
        for index in range(len(yearList)):
            if year1 == yearList[index]:
                yearGenreIndex.append(index)
        year1 = year1 + 1
    #returns the index of every year between the returned year 1 and year 2
    return yearGenreIndex

#insertion sorting algorithm from week 9 algorithm sample code
def insertionSort(theList):
    for i in range(1, len(theList)):
        save = theList[i]
        j = i
        while j > 0 and theList[j - 1] > save:
            theList[j] = theList[j - 1]
            j = j - 1
        theList[j] = save
    return theList

#function for checking for a valid genre
#takes the parameter of the genre list
def validGenre(genreList):
    #loops through genre list until user input genre is true
    while True:
        #asks user for genre
        genre = input("Enter genre: ")
        #loops through genre list
        for filmgenre in genreList:
            #splits genres by semi colon and puts the seperate genre into a list ~ ex: genre;genre;genre ~ [genre, genre, genre]
            wordList = filmgenre.split(";")
            #loops through the small genre genre list and checks if user input genre is true
            for word in wordList:
                if genre == word:
                    #returns genre
                    return genre
        #print statement every time user input genre is false
        print("Invalid entry - Try again")

#function to get genre index at any returned year index
#takes the parameters of years index, genre list, and the user input genre
def genreIndex(yearGenreIndex, genreList, genre):
    #initialize empty genre film index
    genreFilmIndex = []
    #loops through the years index
    for i in yearGenreIndex:
        #at every index the genre is seperated by semicolons into the small list of genres
        texts = genreList[i]
        newTexts = texts.split(";")
        #loops through small list of genres
        #checks if user input genre is at index i
        #appends in genre film index if true
        for word in newTexts:
            if genre == word:
                genreFilmIndex.append(i)
    #current list is sorted by year
    #insertion sort to sort list by the original index
    genreFilmIndex = insertionSort(genreFilmIndex)
    #returns genre film index
    return genreFilmIndex

#function for printing film genre by a range of years results
#takes parameters of genre film index, title list, genre list, director list, year list, runtime list, revenue list
def printGenreSpecificYearRangeSearch(genreFilmIndex, titleList, genreList, directorList, yearList, runtimeList, revenueList):
    print("\nThe films that meet your criteria are:\n")
    print("TITLE".ljust(45), "GENRE".ljust(35), "DIRECTOR".ljust(24), "YEAR".ljust(8), "RUNTIME".ljust(8), "REVENUE(mil)".rjust(12))
    for i in genreFilmIndex:
        print(titleList[i].ljust(45), genreList[i].ljust(35), directorList[i].ljust(24), str(yearList[i]).ljust(8), str(runtimeList[i]).ljust(8), ("$"+str(revenueList[i])).rjust(12))
        
#CHOICE 3 ~ ----------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------

#CHOICE 4 ~ Search for a film by title --------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------

#function to get valid title using binary search
#binary search algorithm from week 9 algorithm analysis
#takes parameter of title list     
def validTitle(titleList):
    #asks user to input title
    title = input("Enter title:\n")
    #initialize title position
    titlePos = 0
    # left side of list    
    left = 0    
    # right side of the list                
    right = len(titleList) - 1
    found = 0
    while right >= left and found == 0:
        m = (left + right) // 2    
        if title < titleList[m]: 
            right = m - 1 
        elif title == titleList[m]: 
            found = 1
            titlePos = m    
        else:    
            left = m + 1
    if found == 0:
        return -1
    else:
        #returns title position
        return titlePos

#function for printing title search results
#takes parameters of genre title position, title list, genre list, director list, year list, runtime list, revenue list
def printTitleSearch(titlePos, titleList, genreList, directorList, yearList, runtimeList, revenueList):
    if titlePos == -1:
        print("No such film exists.")
    else:
        i = titlePos
        print("\nThe film that meets your criteria is:\n")
        print("TITLE".ljust(45), "GENRE".ljust(35), "DIRECTOR".ljust(24), "YEAR".ljust(8), "RUNTIME".ljust(8), "REVENUE(mil)".rjust(12))
        print(titleList[i].ljust(45), genreList[i].ljust(35), directorList[i].ljust(24), str(yearList[i]).ljust(8), str(runtimeList[i]).ljust(8), ("$"+str(revenueList[i])).rjust(12))
        
#CHOICE 4 ~ ---------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

#CHOICE 5 ~ Find average runtime of films with higher revenue than specified value -----------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------

#function for getting average revenue
#takes paramenters of revenue list and runtime list     
def avgRev(revenueList, runtimeList):
    #asks user for limit
    limit = int(input("Enter revenue limit (millions): $"))
    #initialize sum and count
    #sum = to add up run time
    #count = to count how many revenues over the given limit 
    suM = 0
    count = 0
    #loop for adding revenues over the limit and counting also
    for i in range(len(revenueList)):
        if revenueList[i] >= limit:
            suM = suM + runtimeList[i]
            count = count + 1
    if count == 0:
        avg = 0
    else:
        avg = round((suM/count), 2)
    #returns limit and average 
    return limit, avg

#function for printing results
def printAvgRun(limit, avg):
    if avg == 0:
        print("No films have revenue higher than","${:,.2f}".format(limit),"million.")
    else:
        print("The average runtime for films with revenue higher than","${:,.2f}".format(limit), "million is", avg, "minutes.")
        
#CHOICE 5 ~ ------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------

#CHOICE 6 ~ Sort all lists by revenue and write the results to a new file --------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------

#function to get revenue sorted index
#takes the parameter of revenue list
def revSort(revenueList):
    #iniatialize empty revenue list
    #to get current revenue index
    revList1 = []
    #initialize empty sorted revenue index
    revSortIndex = []
    #loop for appending revenue and its index in a mini list in rev list 1
    for i in range(len(revenueList)):
        revList1.append([revenueList[i], i])
    #insertion sort to sort rev list 1 by only revenue 
    revList1 = insertionSort(revList1)
    #loop to access and append all indexes that was sorted by revenue into sorted revenue index
    for j in revList1:
        revSortIndex.append(j[1])
    #return sorted revenue index
    return revSortIndex

#function for writing the data sorted by revenue
#takes parameters of sorted revenue index, title list, genre list, director list, year list, runtime list, revenue list
def revSortFile(revSortIndex, titleList, genreList, directorList, yearList, runtimeList, revenueList):  
    outName = "movies-sorted-rev.csv"
    outFile = open(outName, 'w')
    for i in revSortIndex:
        outFile.write(titleList[i] + "," + genreList[i] + "," + directorList[i] + "," + str(yearList[i]) + "," + str(runtimeList[i]) + "," + str(revenueList[i]) + '\n')
    outFile.close()
    return

#function to print file status
def printFileStatus():
    outName = "movies-sorted-rev.csv"
    print("Sorted data has been written to the file:", outName + ".")
    
#CHOICE 6 ~ ------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------------

#function to get valid choice
def validChoice():
    #initialize good input as false
    goodChoice = False
    #loop for handling user input if not an integer or not in range 
    while goodChoice == False:
        try:
            choice = int(input("Choice ==> "))
            if 1 <= choice <= 7:
                goodChoice = True
            else:
                print("Choice must be between 1 and 7")
        except ValueError:
            print("Invalid entry - Try again")
    #return choice
    return choice

#function to display choices
#return user input choice
def getChoice():
    # This function displays the menu of choices for the user
    # It reads in the user's choice and returns it as an integer
    print("")
    print("Please choose one of the following options:")
    print("1 -- Find all films made by a specified director")
    print("2 -- Find the highest grossing film made in a specific year")
    print("3 -- Find all films made in a given year range in a specified genre")
    print("4 -- Search for a film by title")
    print("5 -- Find average runtime of films with higher revenue than specified value")
    print("6 -- Sort all lists by revenue and write the results to a new file")
    print("7 -- Quit")
    choice = validChoice()
    #return choice
    return choice

#main            
def main():
    titleList, genreList, directorList, yearList, runtimeList, revenueList = getData()
    choice = getChoice()
    while choice != 7:    
        if choice == 1:
            name = validName(directorList)
            directIndex = directorIndex(directorList, name)
            printfilmSearch(directIndex, titleList, genreList, directorList, yearList, runtimeList, revenueList)
            choice = getChoice()
        elif choice == 2:
            year = getYear()
            yearIndex = allYearIndex(year, yearList)
            revIndex = highGrossIndex(yearIndex, revenueList)
            printhighGrossFilm(revIndex, titleList, genreList, directorList, yearList, runtimeList, revenueList)
            choice = getChoice()
        elif choice == 3:
            print("Enter year range to search (oldest year first)")
            year1 = getYear1()
            year2 = getYear2(year1)
            yearGenreIndex = yearGenreSearchIndex(year1, year2, yearList)
            genre = validGenre(genreList)
            genreFilmIndex = genreIndex(yearGenreIndex, genreList, genre) 
            printGenreSpecificYearRangeSearch(genreFilmIndex, titleList, genreList, directorList, yearList, runtimeList, revenueList)
            choice = getChoice()
        elif choice == 4:
            titlePos = validTitle(titleList)
            printTitleSearch(titlePos, titleList, genreList, directorList, yearList, runtimeList, revenueList)
            choice = getChoice()
        elif choice == 5:
            limit, avg = avgRev(revenueList, runtimeList)
            printAvgRun(limit, avg)
            choice = getChoice()
        elif choice == 6:
            revSortIndex = revSort(revenueList)
            revSortFile(revSortIndex, titleList, genreList, directorList, yearList, runtimeList, revenueList)
            printFileStatus()
            choice = getChoice()
        else:
            print("Invalid entry - Try again")
            choice = getChoice()
    print("\nGood-bye")
