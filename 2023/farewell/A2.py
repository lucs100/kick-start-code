# This code was written in official competition by Lucas Di Pietro.
# Practice Attempt 1: 00:13 after competition end // 0/14 Points (4, 10) [WA]
# Practice Attempt 2: 00:22 after competition end // 4/14 Points (4, 10) [TLE]
# See "A2 old iteration.py" for first attempt.

caseCount = int(input())
for i in range(1, caseCount + 1):
    length, radius, count = [int(s) for s in input().split(" ")]
    locations = list(map(int, input().split()))
    locations.sort(reverse=True)

    locks = []

    def getBulbRange(l0):
        global radius
        global length
        return range(max(0, l0-(radius)), (min(length, l0+radius)))

    def getBulbMax(l0):
        global radius
        global length
        return (min(length, l0+radius))
    
    def getNextTest():
        n = getBulbMax(max(locks))
        if n == length:
            return length
        return getBulbMax(max(locks))

    def genLocks():
        global locations
        global length
        global locks

        m = 0
        while m < length:
            OK = False
            for l in locations:
                if not OK:
                    if m in getBulbRange(l):
                        OK = True
                        locks.append(l)
                        locations.remove(l)
                        m = getNextTest()
                        if m == length: return True
                        continue
            if not OK: return False
        return True

    possible = genLocks()
    
    def countLocks(locks0, possible0):
        if not possible0: return "IMPOSSIBLE"
        return len(locks0)

    print("Case #{}: {}".format(i, str(countLocks(locks, possible))))