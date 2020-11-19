caseCount = int(input())
for i in range(1, caseCount + 1):
    intCount, goal = [int(s) for s in input().split(" ")]
    total = 0
    numbers = list(map(int, input().split()))
    while goal in numbers:
        tg = numbers.index(goal)
        for j in range(0, goal-1):
            if numbers[tg+j+1] == goal-(j+1):
                pass
            else:
                break
            total += 1
            break
        numbers.pop(tg)
    print("Case #{}: {}".format(i, total))

    #seems to work but throws runtime error on kick start