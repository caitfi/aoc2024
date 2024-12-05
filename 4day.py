f = open("input/4.txt", "r")
body = f.readlines()


def searchForWordOccurrences(wordToFind, text, x, y):
    rowLength = len(text)
    colLength = len(text[0]) - 1
    numFullWordsFound = 0

    # if we aren't at the start of the word then we don't count
    if (text[x][y] != wordToFind[0]):
        return 0

    searchDirection = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

    for direction in searchDirection:
        currentX = x + direction[0]
        currentY = y + direction[1]
        searchChar = 1

        while searchChar < len(wordToFind):
            # trace the line along this direction
            # if we go out of bounds the word isn't this way
            if currentX >= rowLength or currentX < 0 or currentY >= colLength or currentY < 0:
                # continue to the next direction
                break

            # if this isn't the next letter, wrong way
            if text[currentX][currentY] != wordToFind[searchChar]:
                break

            # it's the right letter, so keep traversing this direction
            currentX += direction[0]
            currentY += direction[1]
            searchChar += 1
        
        if searchChar == len(wordToFind):
            # we found the whole word in this direction
            # on to the next!
            numFullWordsFound += 1

    return numFullWordsFound

def findMasWordCross(text, x, y):
    rowLength = len(text)
    colLength = len(text[0]) - 1

    # only care about the diagonals
    lDia = [[-1, -1], [1, 1]]
    rDia = [[1, -1], [-1, 1]]

    # start with middle coordinate
    if (text[x][y] != "A"):
        return False
    
    # can't make a cross if the text is on the border
    if (x == 0 or y == 0 or x == rowLength - 1 or y == colLength - 1):
        return False
    
    leftDiaWord = text[x + lDia[0][0]][y + lDia[0][1]] + text[x][y] + text[x + lDia[1][0]][y + lDia[1][1]]
    rightDiaWord = text[x + rDia[0][0]][y + rDia[0][1]] + text[x][y] + text[x + rDia[1][0]][y + rDia[1][1]]

    acceptedWords = ["SAM", "MAS"]
    if leftDiaWord in acceptedWords and rightDiaWord in acceptedWords:
        return True
    else:
        return False
    


wordToFind = "XMAS"
numWordsFound = 0
numCrossesFound = 0

for i, line in enumerate(body):
    for j, char in enumerate(body[i]):
        # if we only count each X once, then no dupes
        # BUT each X could have multiple words coming from it
        numWordsFound += searchForWordOccurrences(wordToFind, body, i, j)
        if (findMasWordCross(body, i, j)):
            numCrossesFound += 1

print(numWordsFound)
print(numCrossesFound)