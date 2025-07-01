# # # # # append()  split() pop(index) sort()

# # # # # palindrome list

# # # # a = input("Enter a Arraya:")
# # # # b = input("Enter 2ndd Arraya:")

# # # # arr=[]
# # # # for i in range(3):
# # # #     movie = input("Enter a Arraya:")
# # # #     arr.append(movie)

# # # # print(f"your arr{arr}")

# # # # pal = arr.copy()

# # # # pal.reverse()
# # # # print(pal)
# # # # result =True if pal==arr else False

# # # # print(f"Palindrome Equal to : {result}")

    

# arr=[]
# n = int(input())
# for i in range(4):
#     movie = int(input("Enter a Array:"))
#     arr.append(movie)
# print(arr)
# arr.sort(reverse=True)
# max = arr[0]
# print(max)
# arr.sort(reverse=True)
# for i in arr:
#      if (i<max):
#            ans = i
#            break
     
# print(ans)

# # arr=[]

# # for i in range(1,11): 
    
# #     arr.append(i*i)
# # print(arr) 
# # # arr=[]
# # # for i in range(4):
# # #     movie = int(input("Enter a Array:"))
# # #     arr.append(movie)
# # # print(arr)
# # # target= int(input("Enter Target:"))

# # # for i in range (len(arr)):
# # #     if (arr[i]==target):
# # #         print("True")
# # #         break
# # #     else:
# # #         print("Target not found")
# # #         break
# # # print(i)

# # # def count_substring():
# # #     a = 10
# # #     return a
# # # count = count_substring()
# # # print(count)

# # # if (count=! -1)
# # # count = 0
# # # string = input().strip()
# # # string2 = input().strip()
# # # string.count(string2)
     
# # # print(count)

# # # string = "ABCDCDC"
# # # st_sub = "CDC"
# # # for i in range(0,len(string)):

# # # a = None
# # # set = set()
# # # print(type(set))

# # set ={ "python","java","python","javascript","java","python","c++","c"}
# # count=0
# # for i in set:
# #     count = count+1
# # print(count)

# # text1 = "Hello my name is python"
# # text2 = "hello my is java"
# # setA = set(text1.split(" "))
# # setB= set(text2.split(" "))
# # union = setA.union(setB)

# # print(union)
# # # unique in a not in b
# # unique = setA.difference(setB)
# # unique2= setB.difference(setA)
# # add = setA & setB
# # print(unique)
# # print(unique2)
# # print(add)
# arr=set()
# for i in range(4):
#     movie = int(input("Enter a Array:"))
#     arr.add(movie)
# print(arr)
# result = max(arr)
# print(result)
# arr.remove(result)
# p = max(arr)
# print(p)
#
#  make a list remove the duplicate and convert it to a set , find avg for marks



# list = []
# tuple = ()
# for i in range (3):
#         name = input("Enter your Name: ")
#         marks= int(input("Enter Your marks:"))
#         tuple= (name , marks)
#         list.append(tuple)

# print(list)
# set = set(list)
# print(set)


# marks = 0
# for name, marks in set:
#     marks = marks  + marks 
# average = marks / len(set)
# print(f"Average marks: {average}")


# list1 = [3, 5, 6, 3, 4, 4, 9, 9]
# set1 = set()
# dup = set()
# for i in list1:
#     if i in set1:
#         dup.add(i)
#     else:
#         set1.add(i)
# print(dup)
# dup =set()
# cout=0
# list1 = [3, 5, 6,4, 3, 4, 9, 9]
# for i in range(len(list1)):
#     if  list1[i] in list1[i+1:]:
#          dup.add(list1[i])
# print(dup)

# n = eval("2*2")
# print(n)
# N = int(input())
# list = []
# op = []
# for i in range(N):
#    operation = input().split()
#    op.append(operation)
# print(op)

# print(list[0][1])

# list = list(map ( int , input().split()))
# print(list)
# n = int(input())
# student_marks = {}
# for _ in range(n):
#     name, *line = input().split()
#     scores = list(map(float, line))
#     student_marks[name] = scores
# query_name = input()


# n = int ( input())
# setA= set ( map ( int , input().split()))
# m = int ( input())
# setB = set ( map ( int , input().split()))
# union = setA.difference(setB)
# print(union)

# setA = set()
# n = int (input())
# for i in range (n):
#      a = int (input())
#      setA.add(a)
# length = len(setA)
# print(length)


# dup= set()
# count=0
# list1 = [3,5,6,4,3,4,9,9,9]
# t = 10
# for i in range(len(list1)):
#     if  list1[i] in list1[i+1:]:
#          count = count+1 
#     if count==2:     
#        dup.add(list1[i])
# print(dup)

# find if target = = list1[i]+list1[i+1]



# count=0
# list1 = [3,5,6,4,3,4,9,9,9]
# t = 10
# setA= set()
# for i in range(len(list1)):
#     for j in range(i+1,len(list1)):
#         if list1[i]+list1[j]==t:
#             setA.add((list1[i],list1[j]))
# print(setA)


# student= []
# for _ in range(int(input())):
#     name = input()
#     score = float(input())
#     student.append((name,score))
# grade = sorted({score for name , score in student})  
# second_lowest = grade[1] 
# print(grade)
# names = sorted([name for name, score in student if score == second_lowest])
# second_lowest = grade[1]
# for name in names:
#     print(name)

# # Step 1: Take number of students as input
# n = int(input())

# # Step 2: Create a list to store [name, grade] pairs
# students = []

# # Step 3: Read input for each student
# for _ in range(n):
#     name = input()
#     grade = float(input())
#     students.append([name, grade])

# # Step 4: Extract all unique grades and sort them
# grades = sorted(set([student[1] for student in students]))

# # Step 5: Find the second lowest grade
# second_lowest = grades[1]

# # Step 6: Find all students with the second lowest grade
# second_lowest_students = [student[0] for student in students if student[1] == second_lowest]

# # Step 7: Sort the names alphabetically
# second_lowest_students.sort()

# # Step 8: Print each name
# for name in second_lowest_students:
#     print(name)


# n = int(input())
# student_marks = {}
# for _ in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] = scores
# query_name = input()
# if  query_name = 

# n = int ( input())
# setA= set ( map ( int , input().split()))
# m = int ( input())
# setB = set ( map ( int , input().split()))
# union = setA.symmetric_difference(setB)
# length = len(union)
# print(length)

n = int(input())
for i in range (1,n+1):
     for j in range(1,n-1):
          print(i, end="")
     print()