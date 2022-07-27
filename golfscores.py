#Darryl Alexander Fleurantin
#02/14/2022
#CSC 110 Homework 3 Python lists ~ Part 1

#list to store scores
golfScores = []

#list to store cut golfers
cutOff = []

#ask user for number of golfers
numGolfers = int(input("How many golfers are in the tournament? "))

#for loop for getting scores and appending it in a list 
for i in range(numGolfers):
    score = int(input("Enter two-day score for golfer " + str(i + 1) + ": "))
    golfScores.append(score)
    
#ask user for the cut off score
cut = int(input("Enter the cut-off score: "))

#for loop for appending scores that made the cut
for j in golfScores:
    if j < cut:
        cutOff.append(j)

#calculates the percent of golfers that made the cut
perCent = (len(cutOff) / numGolfers) * 100

#conditional statement for printing the percent of golfers or if there is none
if len(cutOff) != 0:
 print("The percent of golfers that made the cut is " + str(perCent) + " %.")
else:
    print("No golfers made the cut")
