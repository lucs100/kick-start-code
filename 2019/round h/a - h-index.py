
c = int(input())

for i in range(1, c+1):
    p = int(input())
    papers = list(map(int, input().split()))
    curH = 0
    hSet = []

    for j in range(1, p+1):
        if sum((k >= (curH+1)) for k in papers[0:j]) > curH:
            curH += 1
        hSet.append(curH)

    hStr = str(hSet)[1:-1]
    hStr = hStr.replace(",", "")
    
    print(f"Case #{i}: {hStr}")