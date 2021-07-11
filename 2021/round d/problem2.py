# This code was written in official competition by Lucas Di Pietro.
# Attempt 1: 01:09:23 // X/21 Points (9, 12)
def willBeCut(interval, b):
    if interval[0] < b and b < interval[1]:
        return True
    return False

def cutsPossible(intervalList):
    for interval in intervalList:
        if (interval[1] - interval[0]) > 1:
            return True

def findBestX(intervalList):
    lowest = 9999999999999999999
    highest = -1
    for interval in intervalList:
        lowest = min(interval[0], lowest)
        highest = max(interval[1], highest)
    maxCuts = 0
    bestNum = None
    for testNum in range(lowest, highest):
        cuts = 0
        for interval2 in intervalList:
            if willBeCut(interval2, testNum):
                cuts += 1
        if cuts > maxCuts:
            maxCuts = cuts
            bestNum = testNum
    return bestNum

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
    print(intervals)
    for c in range(maxCuts):
        if cutsPossible(intervals):
            point = findBestX(intervals)
            print(point)
            intervals = performCut(intervals, point)
            print(intervals)
        else:
            break
    result = len(intervals)
    print("Case #{}: {}".format(case, result))