caseCount = int(input())
for i in range(1, caseCount + 1):
    countPeople, maxWithdraw = [int(s) for s in input().split(" ")]
    peopleList = list(map(int, input().split()))
    orderList = list(range(countPeople))
    for i in orderList:
        orderList[i] += 1
    finalList = []
    while len(peopleList) != 0:
        peopleList[0] -= maxWithdraw
        if peopleList[0] <= 0:
            finalList.append(orderList[0])
            orderList.pop(0)
            peopleList.pop(0)
        else:
            orderList.append(orderList[0])
            orderList.pop(0)
            peopleList.append(peopleList[0])
            peopleList.pop(0)
    exitOrder = str(finalList).strip("[]")
    print(exitOrder + "done")
    exitOrder = exitOrder.replace(', ', ' ')
    print("Case #{}: {}".format(i, exitOrder))