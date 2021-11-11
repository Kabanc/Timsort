from stack import Stack
from list import List


class Timsort:

    def __init__(self, list: list):
        self.list = list

    @staticmethod
    def sorting(_list):
        minRun = Timsort.getMinRun(len(_list))
        indexRun = 0
        runsData = Stack()
        startIndex, runSize, indexRun = Timsort.getNextRun(_list, indexRun, minRun)

        while runSize is not None and startIndex is not None:
            runsData.push([startIndex, runSize])
            startIndex, runSize, indexRun = Timsort.getNextRun(_list, indexRun, minRun)

        while runsData.__len__() >= 3:
            run1 = runsData.pop()
            run2 = runsData.pop()
            run3 = runsData.pop()

            run1Start = run1[0]
            run2Start = run2[0]
            run3Start = run3[0]

            run1Size = run1[1]
            run2Size = run2[1]
            run3Size = run3[1]

            if run1Size + run2Size < run3Size and run1Size < run2Size:
                runsData.push(run3)
                runsData.push(run2)
                runsData.push(run1)

            elif run2Size + run1Size <= run3Size:
                runsData.push(run1)
                newRun = Timsort.merge(_list, run3Start, run2Start, run3Size, run2Size)

                runsData.push(newRun)

            else:
                newRun = Timsort.merge(_list, run2Start, run1Start, run2Size, run1Size)

                runsData.push(newRun)
                runsData.push(run3)

        while runsData.__len__() == 2:
            run1 = runsData.pop()
            run2 = runsData.pop()

            run1Start = run1[0]
            run2Start = run2[0]

            run1Size = run1[1]
            run2Size = run2[1]

            if run1Size < run2Size:
                newRun = Timsort.merge(_list, run1Start, run2Start, run1Size, run2Size)

            else:
                newRun = Timsort.merge(_list, run2Start, run1Start, run2Size, run1Size)

            runsData.push(newRun)

    @staticmethod
    def getMinRun(n):
        r = 0

        while n >= 64:
            r |= n & 1
            n >>= 1

        return n + r

    @staticmethod
    def insertionSort(startIndex, endIndex, _list):
        n = endIndex - startIndex + 1
        for i in range(1, n):
            key = _list[startIndex + i]
            j = i + startIndex - 1

            while j >= startIndex and _list[j] > key:
                _list[j + 1] = _list[j]
                j -= 1
            _list[j + 1] = key


    @staticmethod
    def reversePart(_list, startIndex, endIndex):
        for i in range((endIndex - startIndex) // 2 + 1):
            if startIndex != endIndex:
                _list[startIndex + i], _list[endIndex - i] = _list[endIndex - i], _list[startIndex + i]

    @staticmethod
    def getNextRun(_list, index, minRun):
        if index is not None:
            if len(_list) - index <= 0:
                return None, None, None
            if len(_list) - index == 1:
                return index, 1, None

            startIndex = index

            el1 = _list[index]
            el2 = _list[index + 1]

            index += 2
            runSize = 2

            if el1 < el2:
                x = el2
                while index < len(_list) and x < _list[index]:
                    x = _list[index]
                    runSize += 1
                    index += 1

                Timsort.reversePart(_list, startIndex, index - 1)
                index += 1
                runSize += 1

            else:
                x = el2

                while index < len(_list) and x >= _list[index]:
                    x = _list[index]
                    runSize += 1
                    index += 1

            if runSize < minRun:
                while index < len(_list) and runSize < minRun:
                        index += 1
                        runSize += 1

                # if index - 1 != len(_list):
                #     runSize -= 1

                index = startIndex + runSize

            Timsort.insertionSort(startIndex, startIndex + runSize - 1, _list)

            return startIndex, runSize, index
        else:
            return None, None, None

    @staticmethod
    def merge(_list, startIndex1, startIndex2, size1, size2):
        tempList = []

        for i in range(startIndex1, startIndex1 + size1):
            tempList.append(_list[i])
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
                _list[curEl] = _list[curEl]
                el2 += 1
            elif el2 == startIndex2 + size2:
                if not last_from_left:
                    last_from_left = True
                    count = 0
                _list[curEl] = tempList[el1]
                el1 += 1
            else:
                if tempList[el1] > _list[el2]:
                    if last_from_left:
                        last_from_left = False
                        count = 0
                    _list[curEl] = _list[el2]
                    el2 += 1
                else:
                    if not last_from_left:
                        last_from_left = True
                        count = 0
                    _list[curEl] = tempList[el1 + 1]
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

                curEl, el1 = Timsort.gallop(_list, tempList, curEl, el1, _list[el2])

            else:
                if el1 == size1:
                    count = 0
                    continue

                current_data, current2 = Timsort.gallop(_list, _list, curEl, el2, tempList[el1])
            last_from_left = not last_from_left
            count = 0
            curEl += 1
        return startIndex1, size1 + size2

    @staticmethod
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


