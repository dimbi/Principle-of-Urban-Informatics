# Functions for students to implement.

def solveWithSet(inputList):
    outputSet = set(inputList)
    return list(outputSet)

def solveOnlyLists(inputList):
    uniqueList = []

    for item in inputList:        
        if not item in uniqueList:
            uniqueList.append(item)
    return uniqueList

def solveDict(inputList):
    uniqueList = {}

    for item in inputList:        
        if not item in uniqueList:
            uniqueList[item] = 1
    return uniqueList.keys()

def solveSorted(inputList):
    uniqueList = []
    previousItem = None
    for item in inputList:
        if item != previousItem:
            previousItem = item
            uniqueList.append(item)
    return uniqueList
