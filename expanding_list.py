def expanding(a):
    d = a[1] - a[0]
    for i in range(2, len(a)):
        b = abs(a[i+1] - a[i])
        i += 1
        if abs(b > d):
            d = b
            return True
        else:
            return False

a = list(map(int,input("Enter the list: ").split()))
out = expanding(a)
print(out)