# Every set of three lines in your list corresponds to a single group, but each group can have a different badge item type. So, in the above example, the first group's rucksacks are the first three lines:

# vJrwpWtwJgWrhcsFMMfFFhFp
# jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
# PmmdzqPrVvPwwTWBwg
# And the second group's rucksacks are the next three lines:

# wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
# ttgJtRGJQctTZtZT
# CrZsJsPPZsGzwwsLwLmpwMDw
# In the first group, the only item type that appears in all three rucksacks is lowercase r; this must be their badges. In the second group, their badge item type must be Z.

# Priorities for these items must still be found to organize the sticker attachment efforts: here, they are 18 (r) for the first group and 52 (Z) for the second group. The sum of these is 70.

# Find the item type that corresponds to the badges of each three-Elf group. What is the sum of the priorities of those item types?

file = open("rucksacks.txt","r")
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
total = 0

for i, line in enumerate (file):
    print(i,line)
    if i % 3 == 0:
        firstLine = line
    if i % 3 == 1:
        secondLine = line
    if i % 3 == 2:
        thirdLine = line
        for c in firstLine:
            if c in secondLine:
                if c in thirdLine:
                    print(firstLine + secondLine + thirdLine + c + "\n\n")
                    total += (characters.index(c) + 1)
                    break
                    

print (total)