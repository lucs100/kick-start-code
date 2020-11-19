caseCount = int(input())
for i in range(1, caseCount + 1):
    intCount, goal = [int(s) for s in input().split(" ")]
    total = 0
    numbers = list(map(int, input().split()))
    if len(numbers) == intCount:
        for k in numbers:
            if numbers[k-1] == goal:
                loopCount = 1
                mode = True
                while goal - loopCount > 0:
                    if numbers[(k-1)+loopCount] - numbers[k+loopCount] == 1:
                        loopCount += 1
                    else:
                        mode = False
                        break
                if mode:
                    total += 1
    print("Case #{}: {}".format(i, total))