# This code was written in official competition by Lucas Di Pietro.
# Attempt 1: 01:09:23 // 0/21 Points (9, 12) [WA]
# Attempt 2: 01:12:41 // 0/21 Points (9, 12) [TLE]
# Attempt 3: 01:57:02 // 0/21 Points (9, 12) [RE]
# Attempt 4: 02:02:02 // 0/21 Points (9, 12) [RE]
# Attempt 5: 02:17:04 // 0/21 Points (9, 12) [TLE]
# Attempt 6 had no changes
# Attempt 7: 02:17:04 // X/21 Points (9, 12) [TLE]

def willBeCut(interval, b):
    if interval[0] < b < interval[1]:
        return True
    return False

def cutsPossible(intervalList):
    for interval in intervalList:
        if (interval[1] - interval[0]) > 1:
            return True

def prune(intervals):
    count = 0
    for interval in intervals:
        if (interval[1] - interval[0]) == 1:
            count += multis[intervals.index(interval)-1]
            intervals.remove(interval)
    return intervals, count

def getMidpt(interval):
    return (interval[0]+interval[1])/2

def getCount(intervals, midpt):
    count = 0
    for interval in intervals:
        if willBeCut(interval, midpt):
            count += multis[intervals.index(interval)-1]
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
            if midpt.is_integer(): #   X.0
                count = getCount(intervalList, midpt)
                midpts[int(midpt)] = count
            else:                  #   X.5
                mp1 = int(midpt)
                count = getCount(intervalList, mp1)
                midpts[mp1] = count
                mp2 = int(midpt) + 1
                count = getCount(intervalList, mp2)
                midpts[mp2] = count

    best = (max(midpts.values()))
    return (list(midpts.keys())[list(midpts.values()).index(best)])

def performCut(intervalList, b):
    for interval in intervalList:
        if willBeCut(interval, b):
            intervalList = list(intervalList)
            intervalIndex = intervalList.index(interval)
            multi = multis[intervalIndex-1]
            interA = [interval[0], b]
            interB = [b, interval[1]]
            intervalList[intervalIndex] = interA
            intervalList.insert(intervalIndex+1, interB)
            multis.insert(intervalIndex+1, multi)
    return intervalList

caseCount = int(input())
for case in range(1, caseCount + 1):
    intervalCount, maxCuts = [int(s) for s in input().split(" ")]
    intervals = list([])
    multis = []
    for interval in range(0, intervalCount):
        inInterval = ([int(s) for s in input().split(" ")])
        if inInterval in intervals:
            multis[intervals.index(inInterval)-1] += 1
        else:
            intervals.append(inInterval)
            multis.append(1)
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