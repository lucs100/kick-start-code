caseCount = int(input())
for i in range(1, caseCount + 1):
    numCount = [int(s) for s in input().split(" ")]
    x = list(map(int, input().split()))
    result = 0
    record = 0
    for m in range(len(x)-1):
        if x[m] > record:
            record = x[m]
            if x[m] > (x[m+1]):
                result += 1
    if x[-1] > record:
        result += 1
    print("Case #{}: {}".format(i, result))