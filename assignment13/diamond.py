x1 = int(input("ernter a number: "))
x = [0,x1,1]
for i in range(2):
    for i in range(x[0],x[1],x[2]):
        print(((x1 - i) * "  "), ((i * 2 - 1) * "💙"), ((x1 - i) * "    "), ((i * 2 - 1) * "💙"))
    x = [x1, 0, -1]