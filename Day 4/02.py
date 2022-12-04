# In the above example, the first two pairs (2-4,6-8 and 2-3,4-5) don't overlap, while the remaining four pairs (5-7,7-9, 2-8,3-7, 6-6,4-6, and 2-6,4-8) do overlap:

# 5-7,7-9 overlaps in a single section, 7.
# 2-8,3-7 overlaps all of the sections 3 through 7.
# 6-6,4-6 overlaps in a single section, 6.
# 2-6,4-8 overlaps in sections 4, 5, and 6.
# So, in this example, the number of overlapping assignment pairs is 4.

# In how many assignment pairs do the ranges overlap?

file = open("Inputs.txt","r")
counter = 0

for line in file:
    overlap = True
    sets = line.split(",")
    set1 = sets[0]
    set2 = sets [1]

    small = int(set1.split("-")[0])
    large = int(set1.split("-")[1])
    small2 = int(set2.split("-")[0])
    large2 = int(set2.split("-")[1])
    for i in range(small,large+1):
        if (i >= small2 and i <= large2):
            counter += 1
            break

print (counter)