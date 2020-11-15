from statistics import geometric_mean
from math import floor, ceil
cases = int(input()) # read a line with a single integer, t is the number of cases
for i in range(1, cases + 1): # number of cases to loop through

    playerCount = int(input())

    totalX, totalY = 0, 0
    xValues = []
    yValues = []

    for n in range(playerCount):
        currentPlayerX, currentPlayerY = [int(s) for s in input().split(" ")]
        totalX += currentPlayerX
        totalY += currentPlayerY
        xValues.append(currentPlayerX)
        yValues.append(currentPlayerY)

    # avgX = round(totalX / playerCount)
    avgY = 0
    

    movement = 0

    gm = (geometric_mean(xValues))

    
    if playerCount % 2 == 0:
        halfArray = int(playerCount/2)
        if gm % 1 != 0:
            sp1 = floor(gm)
            sp2 = ceil(gm)
            for k in range(halfArray):
                movement += abs(abs(sp1 - k) - xValues[0])
                xValues.pop(0)
            for l in range(halfArray):
                movement += abs(abs(sp2 + l) - xValues[0])
                xValues.pop(0)
    else:
        halfMinusMid = int((playerCount-1)/2)
        mp = ceil(len(xValues/2))
        for u in range(halfArray):
            movement += abs(mp - (len((xValues + 1) - 2)) - xValues[0])
    
    # for i in xValues:
    #     movement += abs(i - avgX)
    
    for nums in range(int(playerCount/2)):
        movement += abs(yValues[nums] - avgY)

    print("Case #{}: {}".format(i, movement))