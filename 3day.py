import re
from math import prod

def GetTotalMultiplyInText(textToScan):
    matchingCases = [(int(x), int(y)) for x, y in re.findall(r'mul\(([0-9]+),([0-9]+)\)', textToScan)]
    multiplyTotal = sum([prod(t) for t in matchingCases])
    return multiplyTotal

f = open("input/3.txt", "r")

# just want one big line
textBody = " ".join(line.strip() for line in f) 

# part 1
multiplyTotal = GetTotalMultiplyInText(textBody)
print(multiplyTotal)

# part 2
textBodyDontList = textBody.split("don't()")
multiplySplitTotal = 0

# now have a bunch of chunks - [first part][everything after don't, maybe including a do][...]
for i, chunk in enumerate(textBodyDontList):
    # the first part, we can just scan everything
    textToScan = chunk
    # after that, we need to find if there is a do() in that list, and only read from there on
    if i != 0:
        startPoint = chunk.find("do()")
        if (startPoint == -1):
            # there is no do() command in this chunk, so we can move on
            continue
        else:
            textToScan = chunk[startPoint:]

    multiplySplitTotal += GetTotalMultiplyInText(textToScan)

print(multiplySplitTotal)



