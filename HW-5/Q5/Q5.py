def pyramid(x):
    k = x - 1
    for i in range(x):
        for j in range(k):
            print(end = " ")
        k = k -1
        for a in range(i + 1):
            print("* ", end="")
        print()
        

pyramid(5)