# This code was written in official competition by Lucas Di Pietro.
# Attempt 1: 03:01:46 // 0/14 Points (4, 10) [TLE]
# See A2.py for second attempt.

caseCount = int(input())
for i in range(1, caseCount + 1):
    length, radius, count = [int(s) for s in input().split(" ")]
    length += 1
    locations = list(map(int, input().split()))

    states = dict()
    for t in locations:
        states[t] = True

    redundancy = dict()
    locks = []

    def getBulbRange(l0):
        global radius
        global length
        return range(max(0, l0-(radius-1)), (min(length, l0+radius+1)))

    def getLockedRange():
        global locks
        lockedRange = []
        for x in locks:
            for y in getBulbRange(x):
                lockedRange.append(y)
        return lockedRange

    def genRedundancies():
        global radius
        global locations
        global length
        global states
        global locks

        newRedundancy = dict()
        for m in range(1, length):
            if m in getLockedRange():
                print(f"M{m} locked, skipping...")
            else:
                print(f"Starting M{m}...")
                currentMetre = []
                for l in locations:
                    if states[l]:
                        if m in getBulbRange(l):
                            currentMetre.append(l)
                if len(currentMetre) == 1:
                    locks.append(currentMetre[0])
                newRedundancy[m] = currentMetre
        return newRedundancy

    def checkOptimized(redundancy0):
        global length
        global radius
        global locks
        global locations
        OPTIMIZED = 1
        for k, v in redundancy0:
            if len(v) == 0:
                return 2
            if len(v) == 1:
                if v[0] not in locks:
                    locks.append(v[0])
        for l in locations:
            if OPTIMIZED:
                if l not in locks:
                    OK = True
                    for m in getBulbRange(l):
                        if m == length-1:
                            break
                        if not (len(redundancy0[m]) > 1): 
                            OK = False 
                            break
                    if OK:
                        states[l] = False
                        OPTIMIZED = False
        return OPTIMIZED
    
    def optimizeRedundancies(redundancy0):
        newRedundancy = dict()
        for k, v in redundancy0:
            if len(v) != 1:
                newRedundancy[k] = v
        return newRedundancy

    firstRun = False
    possible = True
    redundancy = genRedundancies()
    done = checkOptimized(redundancy)
    # while done == 0 and possible == True:
    #     redundancy = optimizeRedundancies(redundancy)
    #     done = checkOptimized(redundancy)
    if done == 2:
        possible = False
        

    # def countLightsOn(states0, possible0):
    #     if not possible0: return "IMPOSSIBLE"
    #     count = 0
    #     for s in states0.values():
    #         if s == True:
    #             count += 1
    #     return count
    
    def countLocks(locks0, possible0):
        if not possible0: return "IMPOSSIBLE"
        return len(locks0)

    print("Case #{}: {}".format(i, str(countLocks(locks, possible))))