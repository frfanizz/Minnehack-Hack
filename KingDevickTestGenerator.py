import random as rand
import re

# Constant for width of test (in chars)
testWidth = 5
testSpacing = 5
testRows = 8
testColumns = 5

def generateTest(testVersion = 1):
    """
    Generate a King-Devick Test
    """
    spacer = " "
    if testVersion == 1 :
        spacer = "-"
    else :
        spacer = " "
    output = ""
    outputSoln = ""
    for row in range(testRows) :
        rowLocs = generateRowLocs()
        rowLocs.sort()
        rowLocs = rowLocs[0:-1]
        output += str(rand.randint(0,9))
        for currPos in range(testWidth) :
            output += spacer * testSpacing
            if currPos in rowLocs :
                output += (str(rand.randint(0,9)))
            else :
                output += spacer
        output += spacer * testSpacing + str(rand.randint(0,9)) + "\n"
        if testVersion == 1 or testVersion == 2 :
            output += "\n"
    for char in output :
        if char.isdigit() :
            outputSoln += char
    return output, outputSoln

def generateRowLocs() :
    rowLocs = [testWidth]
    while len(rowLocs) < testColumns - 1 :
        currLoc = int(testWidth * rand.random())
        if currLoc not in rowLocs :
            rowLocs.append(currLoc)
    return rowLocs
# ex: [3, 5, 8, 10]


# import KingDevickTestGenerator as kd; kd.generateTest(testVersion = 1); kd.generateTest(testVersion = 2); kd.generateTest(testVersion = 3)
