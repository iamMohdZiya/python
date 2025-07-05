

def bubbly3(a):
    n=len(a)-1
    for i in range(n): 
        for j in range(n-i):
             if a[j] > a[j+1]:
                a[j+1],a[j]= a[j],a[j+1]
    return a

def bubbly4(a):
    n=len(a)-1
    for i in range(n): 
        for j in range(n-i):
             if a[j] < a[j+1]:
                a[j+1],a[j]= a[j],a[j+1]
    return a

def bubbly2(a):
    for i in range(len(a)): 
        for j in range(1,len(a)-i):
            if a[j-1] > a[j]:
                a[j-1],a[j]= a[j],a[j-1]
    return a

def bubbly(a):
    for i in range(len(a)-1): 
        for j in range(len(a)-1):
            if a[j] > a[j+1]:
                a[j+1],a[j]= a[j],a[j+1]
    return a 



a = [9,3,4,2,7,4,2,8]
sortedArray = bubbly(a)
sortedArray2= bubbly4(a)

print(a)
print(a)
