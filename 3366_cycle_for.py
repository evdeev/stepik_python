a, b, c, d = int(input()), int(input()), int(input()), int(input())

sep = '\t'
if a<=10 and b<=10 and c<=10 and d<=10 and a<=b and c<=d:
    print("", end=sep)
    for i in range(c, d+1):
        print(i, end=sep)
    print()

    for j in range(a, b+1):
        print(j, end=sep)
        for i in range(c,d+1):
            print(i*j, end=sep)
        print()
