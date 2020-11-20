caseCount = int(input())
for i in range(1, caseCount + 1):
    playerCount, maxPlayers = [int(s) for s in input().split(" ")]
    playerList = list(map(int, input().split()))
    playerList.sort(reverse=True)
    subsets = []
    thisHours = 0
    for k in range(0, len(playerList)-maxPlayers+1):
        subsets.append(playerList[0+k:(maxPlayers+k)])
    for j in range(len(subsets)):
        thisHours = 0
        goal = max(subsets[j])
        for m in range(len(subsets[j])):
            if subsets[j][m] != goal:
                thisHours += (goal - (subsets[j][m]))
        subsets[j] = thisHours
    print("Case #{}: {}".format(i, min(subsets)))