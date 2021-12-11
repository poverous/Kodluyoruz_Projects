def reverseList(inputList):
    for i in inputList[::-1]:
        if type(i[0]) is list:
            reverseList(i)
        else:
            reversedList.append(i[::-1])

inputList = [[1, 2], [3, 4], [5, 6, 7], [[8, 9, 10]]]
reversedList = []

reverseList(inputList)
print(reversedList)