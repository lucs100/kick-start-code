
c = int(input())

for i in range(1, c+1):
    string = input()
    kick = 0
    occ = 0
    for j in range(len(string)-4):
        if string[j:j+4] == "KICK":
            kick += 1
        elif string[j:j+5] == "START":
            occ += kick
    print(f"Case #{i}: {occ}")