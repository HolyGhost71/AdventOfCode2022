# As you watch the crane operator expertly rearrange the crates, you notice the process isn't following your prediction.

# Some mud was covering the writing on the side of the crane, and you quickly wipe it away. The crane isn't a CrateMover 9000 - it's a CrateMover 9001.

# The CrateMover 9001 is notable for many new and exciting features: air conditioning, leather seats, an extra cup holder, and the ability to pick up and move multiple crates at once.

stacks = [["T","V","J","W","N","R","M","S"],
        ["V","C","P","Q","J","D","W","B"],
        ["P","R","D","H","F","J","B"],
        ["D","N","M","B","P","R","F"],
        ["B","T","P","R","V","H"],
        ["T","P","B","C"],
        ["L","P","R","J","B"],
        ["W","B","Z","T","L","S","C","N"],
        ["G","S","L"]]

file = open("Stacks.txt","r")

for line in file:
    command = line.split(" ") # Indexes: 1 = Move, 3 = from, 5 = to
    for i in range(0, int(command[1])):
        removed = stacks[int(command[3]) - 1].pop(0)
        stacks[int(command[5]) - 1].insert(i,removed)


message = ""
for l in stacks:
    message += l[0]

print (message)
