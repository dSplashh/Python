
#Darryl Alexander Fleurantin
#02/14/2022
#CSC 110 Homework 3 Python lists ~ Part 2

#list to store names

golfNames = []

#list to store scores

golfScores = []

#list to store reverse list from least to greatest

p = []

#ask user to input number of golfers

golfers = int(input("How many golfers are in the tournament? "))

#for loop for getting golfers names with scores appending in a list 

for i in range(golfers):

    names = input("Enter name of golfer" + str(i + 1) + ": ")

    scores = input("Enter score for golfer" + str(i + 1) + ": ")

    golfNames.append(names)

    golfScores.append(scores)

    p.append(scores)

    p.sort(reverse = False)

#for loop for getting the lowest at its index and using that index to get the name also

for k in range(len(golfScores)):

    if p[0] == golfScores[k]:

        n = golfNames[k]

#print the output
        
print("The current leader of the tournament is " + n + "with a score of " + p[0])
