# They do, however, have a drawing of the starting stacks of crates and the rearrangement procedure (your puzzle input). For example:

#     [D]    
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 

# move 1 from 2 to 1
# move 3 from 1 to 3
# move 2 from 2 to 1
# move 1 from 1 to 2
# In this example, there are three stacks of crates. Stack 1 contains two crates: crate Z is on the bottom, and crate N is on top. Stack 2 contains three crates; from bottom to top, they are crates M, C, and D. Finally, stack 3 contains a single crate, P.

# Then, the rearrangement procedure is given. In each step of the procedure, a quantity of crates is moved from one stack to a different stack. In the first step of the above rearrangement procedure, one crate is moved from stack 2 to stack 1, resulting in this configuration:

# [D]        
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 
# In the second step, three crates are moved from stack 1 to stack 3. Crates are moved one at a time, so the first crate to be moved (D) ends up below the second and third crates:

#         [Z]
#         [N]
#     [C] [D]
#     [M] [P]
#  1   2   3
# Then, both crates are moved from stack 2 to stack 1. Again, because crates are moved one at a time, crate C ends up below crate M:

#         [Z]
#         [N]
# [M]     [D]
# [C]     [P]
#  1   2   3
# Finally, one crate is moved from stack 1 to stack 2:

#         [Z]
#         [N]
#         [D]
# [C] [M] [P]
#  1   2   3
# The Elves just need to know which crate will end up on top of each stack; in this example, the top crates are C in stack 1, M in stack 2, and Z in stack 3, so you should combine these together and give the Elves the message CMZ.

# After the rearrangement procedure completes, what crate ends up on top of each stack?

# [T] [V]                     [W]    
# [V] [C] [P] [D]             [B]    
# [J] [P] [R] [N] [B]         [Z]    
# [W] [Q] [D] [M] [T]     [L] [T]    
# [N] [J] [H] [B] [P] [T] [P] [L]    
# [R] [D] [F] [P] [R] [P] [R] [S] [G]
# [M] [W] [J] [R] [V] [B] [J] [C] [S]
# [S] [B] [B] [F] [H] [C] [B] [N] [L]
#  1   2   3   4   5   6   7   8   9 

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
        stacks[int(command[5]) - 1].insert(0,removed)


message = ""
for l in stacks:
    message += l[0]

print (message)

