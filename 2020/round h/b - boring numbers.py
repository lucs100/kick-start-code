cases = int(input())
for i in range(1, cases + 1):
    start, end = [int(s) for s in input().split(" ")]

    def isBoring(x):
        for i in range(1, len(str(x))+1):
            test = int(str(x)[i-1])
            if i % 2 == test % 2:
                pass
            else:
                return False
        return True
    
    countBoring = 0

    for j in range(start, end+1):
        if isBoring(j) == True:
            countBoring += 1

    print("Case #{}: {}".format(i, countBoring))