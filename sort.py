from stack import Stack


# def Timsort(list: list):


def getMinRun(n):
    r = 0

    while n >= 64:
        r |= n & 1
        n >>= 1

    return n + r


def insertionSort(startIndex, endIndex, list):
    n = endIndex - startIndex
    for i in n:
        j = i + startIndex
        while j > 0 and list[j - 1] > list[j]:
            list[j - 1], list[j] = list[j], list[j - 1]


def reversePart(list, startIndex, endIndex):
    for i in range((endIndex - startIndex) // 2 + 1):
        if startIndex != endIndex:
            list[startIndex + i], list[endIndex - i] = list[endIndex - i], list[startIndex + i]


def nextRun(list, index, minRun):
    if len(list) - index <= 0:
        return None
    if len(list) - index == 1:
        return index, 1

    startIndex = index

    el1 = list[index]
    el2 = list[index + 1]
    index += 2
    runSize = 2

    if el1 < el2:
        x = el2
        while index < len(list) and x < list[index]:
            x = list[index]
            runSize += 1
            index += 1
        index += 1
        runSize += 1
    else:
        x = el2
        while index < len(list) and x >= list[index]:
            x = list[index]
            runSize += 1
            index += 1
        index += 1
        runSize += 1

    if runSize < minRun:
        while index < len(list) and runSize < minRun:
            index += 1
            runSize += 1
        # index += 1

    insertionSort(startIndex, startIndex + runSize - 1, list)


def Merge(list, startIndex1, startIndex2, size1, size2):
    tempArr = []
    for i in range(startIndex1, startIndex1 + size1):
        tempArr.append(list[i])
# To be continued
