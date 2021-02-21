
c = int(input())

def opt(m, x, y):
    return(max(opt(m, x+1, y+1), opt(m, x-1, y-1)))
    # idk

for i in range(1, c+1):
    s = int(input())
    grid = [[0 for j in range(s)] for k in range(s)]
    for j in range(s):
        grid[j] = list(map(int, input().split()))
    print(opt(grid, 0, 0))

    
