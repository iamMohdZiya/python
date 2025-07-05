a = [8,4,6,0,3,5,2]

print(a)
def selection_sort(a):
    n = len(a)
    for i in range(n):
        minA = a[i]
        min = i
        for j in range(i+1,n):
            if minA > a[j]:
                minA = a[j]
                min = j
        a[i], a[min] = a[min], a[i]
    print(a)
selection_sort(a)

