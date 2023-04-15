# This code was written in official competition by Lucas Di Pietro.
# Attempt 1: 01:19:08 // 0/29 Points (9, 20) [WA]
# Attempt 1: 01:50:44 // 29/29 Points (9, 20)


caseCount = int(input())
for i in range(1, caseCount + 1):
    target = int(input())

    reps = (target-1)//26
    residual = target - (reps*26)

    def repsToSize(reps):
        sizeCounter = 1
        while reps >= sizeCounter:
            reps -= sizeCounter
            sizeCounter += 1
        return sizeCounter, reps
    
    size, cyclesIn = repsToSize(reps)
    residual += (cyclesIn*26)

    def getTargetInMaster(size0, residual0):
        if size0 == 1:
            return residual0
        else:
            return -(-residual0 // size0)
    
    def getChar(num):
        return (chr(num+96).upper())

    print("Case #{}: {}".format(i, getChar(getTargetInMaster(size, residual))))