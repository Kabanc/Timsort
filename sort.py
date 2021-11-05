from stack import Stack
from run import Run


def Timsort(list):
    minRun = getMinRun(len(list))
    index = 0
    run = Run()
    flag = True
    count = 0

    while True:
        run.start_index, run.size, index = nextRun(list, index, minRun)

        if run.size is None:
            break
        if run.startIndex is None:
            break

        if flag:
            runs = Stack(run)
            flag = False
        else:
            runs.push(run)
            print(runs)

        count += 1

        if count == 10:
            break

    while runs.__len__() >= 3:
        x = runs.pop().data
        y = runs.pop().data
        z = runs.pop().data

        if z.size > x.size + y.size and y.size > x.size:
            runs.push(z)
            runs.push(y)
            runs.push(x)
            break

        if z.size >= x.size + y.size:
            newRun = Run()
            if z.size > x.size:
                runs.push(x)

                newRun.startIndex, newRun.size = merge(list, z.startIndex, z.size, y.startIndex, y.size)
            else:
                runs.push(z)
                newRun.start_index, newRun.size = merge(list, x.startIndex, x.size, y.startIndex, y.size)
            runs.push(newRun)
        else:
            newRun = Run()
            newRun.startIndex, newRun.size = merge(list, y.startIndex, y.size, x.startIndex, x.size)
            runs.push(newRun)

            runs.push(z)

    while runs.__len__() >= 2:
        x = runs.pop().list
        y = runs.pop().list

        newRun = Run()
        newRun.start_index, newRun.size = merge(list, x.start_index, x.size, y.start_index, y.size)
        runs.push(newRun)


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


def merge(list, startIndex1, startIndex2, size1, size2):
    tempList = []
    for i in range(startIndex1, startIndex1 + size1):
        tempList.append(list[i])
    el1 = 0
    el2 = startIndex2

    last_from_left = False
    count = 0

    until = startIndex2 + size2 - 1
    curEl = startIndex1
    while curEl <= until:

        if el1 == size1:
            if last_from_left:
                last_from_left = False
                count = 0
            list[curEl] = list[curEl]
            el2 += 1
        elif el2 == startIndex2 + size2:
            if not last_from_left:
                last_from_left = True
                count = 0
            list[curEl] = tempList[el1]
            el1 += 1
        else:
            if tempList[el1] > list[el2]:
                if last_from_left:
                    last_from_left = False
                    count = 0
                list[curEl] = list[el2]
                el2 += 1
            else:
                if not last_from_left:
                    last_from_left = True
                    count = 0
                list[curEl] = tempList[el1 + 1]
                el1 += 1
        count += 1

        if count != 7:  # GallopSize
            curEl += 1
            continue

        curEl += 1
        if last_from_left:
            if el2 == startIndex2 + size2:
                count = 0
                continue

            curEl, el1 = gallop(list, tempList, curEl, el1, list[el2])

        else:
            if el1 == size1:
                count = 0
                continue

            current_data, current2 = gallop(list, list, curEl, el2, tempList[el1])
        last_from_left = not last_from_left
        count = 0
        curEl += 1
    return startIndex1, size1 + size2


def gallop(list1, list2, curEl, index, comparedEl):
    start_index = index

    i = 0
    while index < len(list2) and list2[index] < comparedEl:
        i += 1
        index += 1 << i

    if i == 0:
        curEl -= 1
        return curEl, index

    index -= 1 << i

    for i in range(start_index, index - start_index + 1):
        list1[curEl] = list2[i]
        curEl += 1

    curEl += index - start_index
    index += 1
    return curEl, index
