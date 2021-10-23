def transposematrix(x):
    a = len(x)
    b = len(x[0])
    y = []
    for i in range(b):
        list = []
        for j in range(a):
            list.append(x[j][i])
        print(list)

transposematrix([[10,8], [2,4],[1,7]])