def palindrome(x):
    n = 0
    m = len(x)
    for i in range(m):
        if (x[i]==x[m - 1]):
            n = n + 1
            m = m - 1
    if (n == len(x)):
        return True
    else:
        return False

print(palindrome("kayak"))
print(palindrome("hello"))