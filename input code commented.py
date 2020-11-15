# input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# This is all you need for most Kick Start problems.
t = int(input()) # read a line with a single integer, t is the number of cases
for i in range(1, t + 1): # number of cases to loop through
    n, m = [int(s) for s in input().split(" ")] # read a list of integers separated by spaces, 2 in this case, split by a space
    print("Case #{}: {} {}".format(i, n + m, n * m)) # {} is each variable to print, represented by .format(a, b, c)
    # in this case, i is the case number, n + m is the first return, and n * m is the second return
    # check out .format's specification for more formatting options