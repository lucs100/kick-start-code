# This code was written in official competition by Lucas Di Pietro.
# Attempt 1: 01:09:23 // 0/21 Points (9, 12) [WA]
# Attempt 2: 01:12:41 // 0/21 Points (9, 12) [TLE]
# Attempt 3: 01:57:02 // X/21 Points (9, 12) [TLE]
def willBeCut(interval, b):
    if interval[0] < b < interval[1]:
        return True
    return False

def cutsPossible(intervalList):
    for interval in intervalList:
        if (interval[1] - interval[0]) > 1:
            return True

def getMidpt(interval):
    return (interval[0]+interval[1])/2

def getCount(intervals, midpt):
    count = 0
    for interval in intervals:
        if willBeCut(interval, midpt):
            count += 1
    return count

def findBestX(intervalList):
    lowest = 9999999999999999999
    highest = -1
    midpts = dict()

    for interval in intervalList:
        lowest = min(interval[0], lowest)
        highest = max(interval[1], highest)
        midpt = getMidpt(interval)
        if isinstance(midpt, int):
            count = getCount(intervalList, midpt)
            midpts[int(midpt)] = count
        if isinstance(midpt, float):
            if midpt.is_integer():
                count = getCount(intervalList, midpt)
                midpts[int(midpt)] = count
    best = (max(midpts.values()))
    return (list(midpts.keys())[list(midpts.values()).index(best)])

def performCut(intervalList, b):
    for interval in intervalList:
        if willBeCut(interval, b):
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
    for c in range(maxCuts):
        if cutsPossible(intervals):
            point = findBestX(intervals)
            intervals = performCut(intervals, point)
        else:
            break
    result = len(intervals)
    print("Case #{}: {}".format(case, result))