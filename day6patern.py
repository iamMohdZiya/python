for row in range(4):
    for column in range(row):
        print("* ",end="")
    print()




for row in range(4):
    for column in range(3,row,-1):
        print("* ",end="")
    print()




for row in range(1,4+1):
    for column in range(4-row):
        print(" ",end="") 
    for star in range(1,row):
        print("* ",end="")
    print()



for i in range(1,5+1):
    for i in range(1,i+1)   :
        print(i,end="")   
    print() 



for i in range(1,5+1):
    for j in range(i):
        print(i,end="")
    print()



st= "ABCDE"

for row in range(0,len(st)):
    for column in range(row+1):
        print(st[row],end="")
    print()

for i in range(1,5+1):
    for j in range(1,i+1):
        print(chr(row+64),end="")
    print()


for i in range(1,5+1):
    for i in range(5,i,-1):
        print(i,end=" ")   
    print() 


for i in range(5+1,0,-1):
    for j in range(0,i):
        print(i,end="")
    print()


# rows
for i in range(5,0,-1):
    # space
    for space in range(i-1,0,-1):
        print(" ",end="")
    
    for j in range(5,i-space,-1):
        print(i,end="")
    print()

for rows in range(1,5+1):
    for column in range(1,5+1):
        if (rows==1 or column== 1 or column ==5 or rows==5):
            print("*",end="")
        else:
            print(" ",end="")

    print() 



n = 6
for row in range(1,n+1):
  for space in range(1,row): # can put 0 , n-1 == 1 ,row 
       print(" ",end="")
  for column in range(1,n-row+1):
       print("*",end="")
  print()


for row in range(n):
    for space in range(1,row): # can put 0 , n-1 == 1 ,row 
       print(" ",end="")
    for column in range(n,row-1,-1):
        print("* ",end="")
    print()

 
for row in range(1,n+1):
    for column in range(n-row):
        print(" ",end="") 
    for star in range(1,row):
        print("* ",end="")
    print()
for row in range(1,n+1):
  for space in range(1,row): # can put 0 , n-1 == 1 ,row 
       print(" ",end="")
  for column in range(n,row,-1):
       print("* ",end="")
  print()
        





for row in range(1,n+1):
  for space in range(1,row): # can put 0 , n-1 == 1 ,row 
       print(" ",end="")
  for column in range(1,n-row+2):
       print(column,end="")
  print()

