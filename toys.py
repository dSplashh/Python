
#Darryl Alexander Fleurantin
#02/28/2022
#CSC 110 Homework 4 Working with Python Functions ~ Part 1

#function to store toy name, price, and how many was sold
def getToys():
    toyNum = int(input("How many toys are in your catalog? "))
    toyName = []
    toyPrice = []
    toySold = []
    for i in range(toyNum):
        name = input("Enter toy name: ")
        price = float(input("Enter toy price: "))
        sold = int(input("Enter number sold: "))
        toyName.append(name)
        toyPrice.append(price)
        toySold.append(sold)
    return toyName, toyPrice, toySold

#function to check toy search by returning its index
def searchToy(toyName, search):
    searchIndex = -1
    for i in range(len(toyName)):
        if toyName[i] == search:
            searchIndex = i
    return searchIndex

#function to check what was sold more than the toy at the index
def soldMore(toyName, toySold, searchIndex):
    soldmoreList = []
    for i in range(len(toySold)):
        if toySold[searchIndex] < toySold[i]:
            soldmoreList.append(toyName[i])
    return soldmoreList

#prints if toy is not identified or if it is it prints the price of the toy with how many toys sold more if any
def printResults(searchIndex, toyName, toyPrice, soldmoreList):
    if searchIndex != -1:
        print("The price of ", toyName[searchIndex], "is $", "{:,.2f}".format(toyPrice[searchIndex]))
        if len(soldmoreList) != 0:
            print("The toys that have more sold than ", toyName[searchIndex], "are: ")
            print(*soldmoreList, sep = '\n') 
        else:
            print("No toys have sold more than ", toyName[searchIndex])
    else:
        print("The toy name you entered is not in our catalog.") 
    return
        
def main():
    toyName, toyPrice, toySold = getToys()
    search = input("Enter a toy to find the price of: ")
    searchIndex = searchToy(toyName, search)
    soldmoreList = soldMore(toyName, toySold, searchIndex)
    printResults(searchIndex, toyName, toyPrice, soldmoreList)
