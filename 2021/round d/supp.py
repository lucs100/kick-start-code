f = open("demofile3.txt", "a")
for int in range(500):
    f.write(f"{int} {int+9499}\n")
f.close()