# This code was written in official competition by Lucas Di Pietro.
# Attempt 1: 00:35:09 // 0/14 Points (6, 8) [WA]
# Attempt 2: 01:11:38 // 14/14 Points (6, 8)
def isArtithmetic(a, b, c):
    return (a - b) == (b - c)

def countGivenSeq(g):
    count = 0
    lines = [
    (g[0][0], g[0][1], g[0][2]),
    (g[0][0], g[1][0], g[2][0]),
    (g[0][2], g[1][2], g[2][2]),
    (g[2][0], g[2][1], g[2][2])]
    for line in lines:
        if isArtithmetic(*line):
            count += 1
    return count

def solve(a, c):
    return ((a+c)/2)

def findOptimal(g):
    opts = []
    lines = [
    (g[0][0], g[2][2]),
    (g[0][1], g[2][1]),
    (g[1][0], g[1][2]),
    (g[2][0], g[0][2])]
    for uline in lines:
        soln = solve(*uline)
        if isinstance(soln, int):
            opts.append(int(soln))
        if isinstance(soln, float):
            if soln.is_integer():
                opts.append(int(soln))
    best = 0
    for num in opts:
        best = max(opts.count(num), best)
    return best

caseCount = int(input())

for case in range(1, caseCount + 1):
    x = list(map(int, input().split())) # row 0
    y = list(map(int, input().split())) # row 1
    y.append(y[1])
    y[1] = None
    z = list(map(int, input().split())) # row 2
    grid = [x, y, z]
    base = countGivenSeq(grid)
    new = findOptimal(grid)
    result = base + new
    print("Case #{}: {}".format(case, result))