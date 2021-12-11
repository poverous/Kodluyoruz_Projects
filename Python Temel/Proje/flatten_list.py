def flattenList(inputList):
    for i in inputList:
        if type(i) is list:
            flattenList(i)
        else:
            flattenList.append(i)

inputList = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
flattenList = []

flattenList(inputList)
print(flattenList)