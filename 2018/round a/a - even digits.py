
cases = int(input())

def isEvens(n):
    x = str(n)
    for i in range(len(x)):
        if int(x[i]) % 2 == 1:
            return False
    return True

def plusser(n):
    count = 0
    while True:
        if isEvens(n):
            return(count)
        n += 1
        count += 1

def minuser(n):
    count = 0
    while True:
        if isEvens(n):
            return(count)
        n -= 1
        count += 1

for i in range(cases):
    number = int(input())
    print("Case #{}: {}".format((i+1), min(plusser(number), minuser(number))))