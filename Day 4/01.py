# Some of the pairs have noticed that one of their assignments fully contains the other. For example, 2-8 fully contains 3-7, and 6-6 is fully contained by 4-6. In pairs where one assignment fully contains the other, one Elf in the pair would be exclusively cleaning sections their partner will already be cleaning, so these seem like the most in need of reconsideration. In this example, there are 2 such pairs.

# In how many assignment pairs does one range fully contain the other?

file = open("Inputs.txt","r")
counter = 0
for line in file:
    contains = True
    sets = line.split(",")
    set1 = sets[0]
    set2 = sets [1]

    small = int(set1.split("-")[0])
    large = int(set1.split("-")[1])
    small2 = int(set2.split("-")[0])
    large2 = int(set2.split("-")[1])
    for i in range(small,large+1):
        if not (i >= small2 and i <= large2):
            contains = False
            break
    
    if not contains:
        contains = True
        for i in range(small2,large2+1):
            if not (i >= small and i <= large):
                contains = False
                break

    if contains:
        counter += 1

print (counter)