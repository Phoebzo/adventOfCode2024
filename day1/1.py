# read txt file 

import pandas 
df = pandas.read_csv('D:\code\Advent of code 2024\day1\locationIds.txt', header = None, delim_whitespace=True)

print (df)

list_1 = df[0].tolist()
list_2 = df[1].tolist()

list_1 = sorted(list_1)
list_2 = sorted(list_2)

addedDiff = 0

for i in range(0, len(list_1)):
    counted_occur = list_2.count(list_1[i])
    print (list_1[i], counted_occur)
    addedDiff = addedDiff + (list_1[i] *counted_occur)

print (addedDiff)