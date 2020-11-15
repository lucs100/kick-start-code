cases = int(input()) # read a line with a single integer, t is the number of cases
for i in range(1, cases + 1): # number of cases to loop through
    levels, currentLevel, goalLevel = [int(s) for s in input().split(" ")]

    downUpCase = currentLevel + (abs(currentLevel-goalLevel)) + abs(goalLevel - levels)
    straightCase = levels + currentLevel

    fastestTime = min(downUpCase, straightCase)

    print("Case #{}: {}".format(i, fastestTime))