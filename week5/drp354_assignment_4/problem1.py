################################################
#****CUSP Principle of urban informatic class**#
#-----Dimas R.Putro / drp354@nyu.edu-----------#
################################################

def solveOnlyLists(inputList):
    uniqueList = []
    for i in inputList:
        if i in uniqueList:
            pass
        else:
            uniqueList.append(i)
    return uniqueList

def solveDict(inputList):
    uniqueList = []
    uniqueList_d = {}
    for i in inputList:
        if i in uniqueList_d:
            pass
        else:
            uniqueList_d[i]=1
    uniqueList = list(uniqueList_d.keys())
    return uniqueList

def solveSorted(sortedInputList):
    uniqueList = []
    token = -1
    for i in sortedInputList:
        if i is not token:
            token = i
            uniqueList.append(i)
        else:
            pass
    return uniqueList
