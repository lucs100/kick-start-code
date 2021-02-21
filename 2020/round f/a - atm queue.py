caseCount = int(input())
for i in range(1, caseCount + 1):
    countPeople, maxWithdraw = [int(s) for s in input().split(" ")]
    line = []
    inputs = [int(s) for s in input().split(" ")]
    for j in range(len(inputs)):
        line.append([j+1, inputs[j]])
    exitOrder = []
    while len(line) != 0:
        cash = line[0][1]
        cash -= maxWithdraw
        if cash > 0:
            line.append([line[0][0], cash])
            line.pop(0)
        else:
            exitOrder.append(line[0][0])
            line.pop(0)
    exitStr = ""
    for j in range(countPeople):
        exitStr += str(exitOrder[j])
        exitStr += " "
    print("Case #{}: {}".format(i, exitStr[:-1]))