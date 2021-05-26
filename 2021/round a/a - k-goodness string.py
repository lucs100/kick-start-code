caseCount = int(input())
for i in range(1, caseCount + 1):
    size, goal = [int(s) for s in input().split(" ")]
    string = input()
    k = 0
    if size > 1:
        for j in range(size):
            if string[j] != string[-j+1]:
                k += 1
        k = int(k/2)
        if size % 2 == 1:
            k -= 1
    result = abs(k - goal)
    print("Case #{}: {}".format(i, result))