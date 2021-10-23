def check(x,y):
    edit = 0
    if (len(x)>=len(y)):
        for i in x:
            if (i not in y):
                edit = edit + 1
    else:
        for j in y:
            if (j not in x):
                edit = edit + 1
    if (edit <= 1):
        return True
    else:
        return False
    

a = "pale"
b = "ple"
c = "pales"
d = "bale"
e = "bake"

print(check(a,b))
print(check(c,a))
print(check(a,d))
print(check(a,e))