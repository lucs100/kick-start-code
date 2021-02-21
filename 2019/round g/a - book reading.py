
import math 

t = int(input())

for i in range(1, t+1):
    countPages, countTorn, countReaders = list(map(int, input().split()))
    pagesGone = list(map(int, input().split()))
    readerMults = list(map(int, input().split()))
    read = 0

    for j in range(len(readerMults)):
        read += math.floor(countPages / readerMults[j])
        for k in range(len(pagesGone)):
            if pagesGone[k] % readerMults[j] == 0:
                read -= 1
    
    print(f"Case #{i}: {read}")