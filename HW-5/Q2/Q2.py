punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

def removepunctuations(x):
    for i in x:
        for j in punctuations:
            if (i==j):
                x = x.replace(i, "")
    return x

print(removepunctuations("Hello in 36-650, & other MSP courses."))