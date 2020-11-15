caseCount = int(input())
for case in range(1, caseCount + 1):

    checkpoints = int(input())

    h = list(map(int, input().split(" ")))

    peaks = 0

    for i in range(1, checkpoints-1):
        if h[i-1] < h[i] and h[i] > h[i+1]:
            peaks += 1 

    print("Case #{}: {}".format(case, peaks))