sort = []
bar = 0
maxCalorie = 0

with open("advent-day-1.txt", "r") as foo:
    elfInput = foo.read()
filteredInput = elfInput.splitlines()

for i in filteredInput:
    if i != "":
        bar += int(i)        
    else:
        sort.append(bar)
        bar = 0
sort.append(bar)

maxCalorie = max(sort)


print(maxCalorie)



# for part 2
maxCalorieSorted = sorted(sort, reverse=True)
maxCalorieSortedTotal = 0

for i in range(3):
    maxCalorieSortedTotal += maxCalorieSorted[i]


print(maxCalorieSortedTotal)