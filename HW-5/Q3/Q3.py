def check1(x, y):
    edit = 0
    for i in x:
        if (i not in y):
            edit = edit + 1    
    if (edit <= 1):
        return True
    else:
        return False
        

def check2(x,y):
    edit = 0
    for j in y:
        if (j not in x):
            edit = edit + 1

    if (edit <= 1):
        return True
    else:
        return False

def check3(x,y):
    edit = 0
    for i in range(len(x)):
        if (x[i]!=y[i]):
            edit = edit + 1
    if (edit <= 1):
        return True
    else:
        return False

def check(x,y):
    if (abs(len(x)-len(y))>1):
        return False
    if (len(x)>len(y)):
        return check1(x,y)
    elif (len(y)>len(x)):
        return check2(x,y)
    else:
        return check3(x,y)
    

a = "pale"
b = "ple"
c = "pales"
d = "bale"
e = "bake"

print(check(a,b))
print(check(c,a))
print(check(a,d))
print(check(a,e))