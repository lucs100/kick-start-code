# Scores 12/12 (5, 7) points

caseCount = int(input())
for i in range(1, caseCount + 1):
    length = int(input())
    testStr = str(input())
    result = []

    def getMaxSubstring(string):
        k = 1
        n = 1
        while k < len(string):
            if string[-k] > string[-(k+1)]:
                n += 1
                k += 1
            else:
                break
        return n

    for j in range(1, length+1):
        result.append(getMaxSubstring(testStr[:j]))

    resultStr = ""
    for n in result:
        resultStr += str(n) + " "
    
    print("Case #{}: {}".format(i, resultStr[:-1]))