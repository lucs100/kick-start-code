# This code was written in official competition by Lucas Di Pietro.
# Attempt 1: 01:09:23 // 0/21 Points (9, 12) [WA]
# Attempt 2: 01:12:41 // 0/21 Points (9, 12) [TLE]
# Attempt 3: 01:57:02 // 0/21 Points (9, 12) [RE]
# Attempt 4: 02:02:02 // 0/21 Points (9, 12) [RE]
# Attempt 5: 02:17:04 // 0/21 Points (9, 12) [TLE]
# Attempt 6 had no changes
# Attempt 7: 03:26:03 // 0/21 Points (9, 12) [TLE]
# Attempt 8: 03:37:34 // 0/21 Points (9, 12) [TLE]
# Attempt 9 failed samples
# Attempt 10: 03:50:22 // 0/21 Points (9, 12) [TLE]

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

def getCount(intervals, midpt):
    count = 0
    for interval in intervals:
        if interval[0] < midpt < interval[1]:
            count += multis[intervals.index(interval)-1]
    return count

def findBestX(intervalList):
    midpts = dict()

    for interval in intervalList:
        midpt = (interval[0]+interval[1])/2
        if isinstance(midpt, int):
            midpts[int(midpt)] = getCount(intervalList, midpt)
        if isinstance(midpt, float):
            if midpt.is_integer(): #   X.0
                midpts[int(midpt)] = getCount(intervalList, midpt)
            else:                  #   X.5
                midpts[int(midpt)] = getCount(intervalList, int(midpt))
                midpts[int(midpt) + 1] = getCount(intervalList, int(midpt) + 1)

    return (list(midpts.keys())[list(midpts.values()).index((max(midpts.values())))])

def performCut(intervalList, b):
    for interval in intervalList:
        if interval[0] < b < interval[1]:
            idx = intervalList.index(interval)
            intervalList[idx] = [interval[0], b]
            intervalList.insert(idx+1, [b, interval[1]])
            multis.insert(idx+1, multis[idx])
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
    print("Case #{}: {}".format(case, result+ len(intervals)))