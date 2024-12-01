from collections import Counter

f = open("input/1.txt", "r")

firstList = []
secondList = []


for line in f:
    twoNumbers = [int(x) for x in line.split() if x.isdigit()]
    firstList.append(twoNumbers[0])
    secondList.append(twoNumbers[1])
    
firstList = sorted(firstList)
secondList = sorted(secondList)

# part 1
distanceTotal = 0

# part 2
similarityScore = 0
countedSecondList = Counter(secondList)

for i in range(len(firstList)):
    # part 1
    distanceTotal += abs(firstList[i] - secondList[i])

    # part 2
    similarityScore += firstList[i] * (countedSecondList[firstList[i]])

print(distanceTotal)
print(similarityScore)
