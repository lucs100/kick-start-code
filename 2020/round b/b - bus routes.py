caseCount = int(input())
for case in range(1, caseCount + 1):
    buses, timeLimit = [int(s) for s in input().split(" ")]

    # input all bus routes
    # only run on multiples of their numbers
    # find latest day to successfully leave

    latestDay = 0

    print("Case #{}: {}".format(case, latestDay))