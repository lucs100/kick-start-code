# Scores 12/12 (5, 7) points

caseCount = int(input())
for caseNumber in range(1, caseCount + 1):
    size, budget = [int(s) for s in input().split(" ")]
    houses = list(map(int, input().split()))
    houses.sort()
    count = 0
    while houses != []:
        if houses[0] <= budget:
            budget -= houses[0]
            houses.pop(0)
            count += 1
        else:
            break
    print("Case #{}: {}".format(caseNumber, count))