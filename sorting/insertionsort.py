a = [ 3,2,56,5454,3,2,8,42,2,6,0,7,8,5,4]

n = len(a)
for i in range(1,n):
    key =a[i]

    j = i-1
    while j >=0 and key < a[j]:
        a[j+1]=a[j]
        j-=1
    
    a[j+1]=key

print(a)
