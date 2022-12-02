# Your total score is the sum of your scores for each round. The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).

# For example, suppose you were given the following strategy guide:

# A Y
# B X
# C Z
# This strategy guide predicts and recommends the following:

# In the first round, your opponent will choose Rock (A), and you should choose Paper (Y). This ends in a win for you with a score of 8 (2 because you chose Paper + 6 because you won).
# In the second round, your opponent will choose Paper (B), and you should choose Rock (X). This ends in a loss for you with a score of 1 (1 + 0).
# The third round is a draw with both players choosing Scissors, giving you a score of 3 + 3 = 6.
# In this example, if you were to follow the strategy guide, you would get a total score of 15 (8 + 1 + 6).

# What would your total score be if everything goes exactly according to your strategy guide?

file = open("Inputs.txt")

score = 0

for line in file:
    choices = line.split(" ")
    pMap = ["X","Y","Z"]
    opMap = ["A","B","C"]
        
    matchup = [[4, 1, 7], [8, 5, 2], [3, 9, 6]]
    
    x = pMap.index(choices[1][0])
    y = opMap.index(choices[0])
    
    score += matchup[x][y]

print(score)