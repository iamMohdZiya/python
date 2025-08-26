

a = [ 2,3,56,5454,3,2,8,42,2,6,0,7,8,5,4]

for i in range(len(a)-1):
    for j in range(len(a)-1):
        if a[j] > a[j+1]:
             a[j+1],a[j]=a[j],a[j+1]
print(a)
