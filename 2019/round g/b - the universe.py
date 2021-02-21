
t = int(input())

for i in range(1, t+1):
    total = 0
    maxK = -1
    intCount, maxTotal = list(map(int, input().split()))
    ints = list(map(int, input().split()))
    for k in range(0, 128):
        total = 0
        for j in range(intCount):
            total += (ints[j] ^ k)
        if total <= maxTotal:
            maxK = k
    
    print(f"Case #{i}: {maxK}")