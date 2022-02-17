from pathlib import Path 

def countChar(fileDataT):
    countChar = 0
    for C in fileDataT:
        if C.isprintable() and C != "\n":
            #print(C)
            countChar += 1
    return countChar

FILE= '/home/mayank/Documents/artical.txt'

with open(FILE,'r') as userFile:
    countLine = 0
    for line in userFile.readlines():
        countLine += 1
        print("Line ", countLine, ",char ",end =" ")
        #print(line)
        countChar = 0
        for charIn in line:
            if charIn != " ": #and charIn != "\n":
                countChar += 1
        print(countChar)

#print(charIn)
#print(countChar(fileData))
#print(countCharPerLine(fileD))
    #print(type(userFile))
    #MyList = userFile.readlines()
    #fileData = userFile.read()
#print(fileData)