t = int(input()) 
for i in range(1, t + 1):
    price = 0
    cards = input()
    for i in range(cards):
        if i == 0:
            shortestCard = len(input())
        if len(input()) < shortestCard:
            shortestCard = len(input())
            price += 1
    print("Case #{}: {}".format(i, price))