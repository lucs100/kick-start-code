# Scores 0/11 (4, 7) points

import math

caseCount = int(input())
for i in range(1, caseCount + 1):
    numCount = [int(s) for s in input().split(" ")]
    numbers = list(map(int, input().split()))
    longest = 0
    streak = 1
    last = float('nan')
    for j in range(1, len(numbers)):
        current = (numbers[j-1] - numbers[j])
        if current == last:
            streak += 1
        elif math.isnan(last):
            streak == 2
        else:
            streak == 1

        longest = max(longest, streak)
        last = current
    print("Case #{}: {}".format(i, longest))