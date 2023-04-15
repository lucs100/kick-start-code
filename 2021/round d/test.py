def willBeCut(interval, b):
    return (interval[0] < b < interval[1])

def prune(intervalList):
    count = 0
    for interval in intervalList:
        if (interval[1] - interval[0]) == 1:
            intervalList.remove(interval)
            count += 1
    return intervalList, count

def cutsPossible(intervalList):
    for interval in intervalList:
        if (interval[1] - interval[0]) > 1:
            return True

def getMidpt(interval):
    return (interval[0]+interval[1])/2

def getCount(intervals, midpt):
    count = 0
    for interval in intervals:
        if (interval[0] < midpt < interval[1]):
            count += 1
    return count

def findBestX(intervalList):
    insta = len(intervalList)
    bestNum = -1
    bestCount = -1

    for interval in intervalList:
        if bestCount == insta:
            return bestNum
        midpt = getMidpt(interval)
        if isinstance(midpt, int):
            count = getCount(intervalList, midpt)
            if count > bestCount:
                bestNum = midpt
                bestCount = count
        if isinstance(midpt, float):
            if midpt.is_integer(): #   X.0
                midpt = int(midpt)
                count = getCount(intervalList, midpt)
                if count > bestCount:
                    bestNum = midpt
                    bestCount = count
            else:                  #   X.5
                mp1 = int(midpt)
                count = getCount(intervalList, mp1)
                if count > bestCount:
                    bestNum = mp1
                    bestCount = count
                mp2 = int(midpt) + 1
                count = getCount(intervalList, mp2)
                if count > bestCount:
                    bestNum = mp2
                    bestCount = count

    return bestNum

def performCut(intervalList, b):
    for interval in intervalList:
        if (interval[0] < b < interval[1]):
            intervalList = list(intervalList)
            intervalList.append([interval[0], b])
            intervalList.append([b, interval[1]])
            intervalList.remove(interval)
    return intervalList

caseCount = int(input())
for case in range(1, caseCount + 1):
    intervalCount, maxCuts = [int(s) for s in input().split(" ")]
    intervals = []
    for interval in range(0, intervalCount):
        intervals.append([int(s) for s in input().split(" ")])
    result = 0
    for c in range(maxCuts):
        if cutsPossible(intervals):
            point = findBestX(intervals)
            intervals = performCut(intervals, point)
            intervals, num = prune(intervals)
            result += num
        else:
            break
    result += len(intervals)
    print("Case #{}: {}".format(case, result))