#Darryl Alexander Fleurantin
#02/14/2022
#CSC 110 Homework 3 Python lists ~ Part 3

#list to store scores

golfScores = []

#list to store scores at rate

rateScore = []

#ask user for how many scores

scoreNum = int(input("How many golf scores have you collected? "))

#for loop to get scores

for i in range(scoreNum):

    scores = int(input("Enter score: "))

    golfScores.append(scores)

rate = int(input("Enter sample rate (k): "))

#for loop to get scores at rate

for j in range(len(golfScores)):

    if j % rate == 0:

        rateScore.append(golfScores[j])
        
print("The sampled scores are:")        
print(rateScore)
