f = open("input/2.txt", "r")

numSafe = 0
numFixable = 0

for line in f:
    reportNums = [int(x) for x in line.split() if x.isdigit()]

    isIncreasingAndAdjacent = all([i < j and j - i in [1,2,3] for i, j in zip(reportNums, reportNums[1:])])
    isDecreasingAndAdjacent = all([i > j and i - j in [1,2,3] for i, j in zip(reportNums, reportNums[1:])])

    # part 1
    if isIncreasingAndAdjacent or isDecreasingAndAdjacent:
        numSafe += 1
    else:
        # part 2
        # ideally I'd like a better solution than iterating over each subset, but I am tired
        for i in range(len(reportNums)):
            subsetList = []
            if (i == 0):
                subsetList = reportNums[1:]
            elif (i == len(reportNums) - 1):
                subsetList = reportNums[:i]
            else:
                subsetList = reportNums[:i] + reportNums[i+1:]
            
            isIncreasingAndAdjacent = all([i < j and j - i in [1,2,3] for i, j in zip(subsetList, subsetList[1:])])
            isDecreasingAndAdjacent = all([i > j and i - j in [1,2,3] for i, j in zip(subsetList, subsetList[1:])])

            if isIncreasingAndAdjacent or isDecreasingAndAdjacent:
                numFixable += 1
                break


print(numSafe)
print(numSafe + numFixable)