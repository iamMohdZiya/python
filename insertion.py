
def insertion(a):
    n = len(a)
    for i in range(n):
        for j in range(i, 0, -1):
            if a[j] < a[j-1]:
                a[j], a[j-1] = a[j-1], a[j]
    return a

a =[8,9,7,4,6,9,3,2,4]
print(a)
r = insertion(a)
print(r)