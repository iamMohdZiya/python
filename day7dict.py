

# # # # # mydict = {
# # # # #     "name":"ziya",
# # # # #     "marks": 99
# # # # # }

# # # # # print(mydict["name"],mydict["marks"])



# # # # mydict = {
# # # #     "name" : "ziya",
# # # #     "marks":{
# # # #         "nodejs":40,
# # # #         "java":90,
# # # #         "python":88
# # # #     }
# # # # }

# # # # print(mydict["name"],mydict["marks"]["python"])



# # # mydict = {
# # #     "table" : {
# # #         "description": "a piece of furniture",
# # #         "facts": [
# # #             "legs",
# # #             " eat",
# # #             "drink"
# # #         ]
# # #     },
# # #     "cat":"a small animal"
# # # }
# # # print(mydict["table"]["facts"])

# # # student = {
           
# # #        }
# # # str1 = input("Enter your name: ")
# # # for i in range (3):
# # #        subject = input("Enter your subject name: ")
# # #        marks =int( input("Enter your marks: "))
# # #        student.update({"name":str1})
# # #        student.update({"marks":subject})
# # #        student.update({subject:marks})
       



# # # name = student.get("name")
# # # keys =student.keys()
# # # values =student.values()
# # # print(values)
# # # print(keys)
# # # print(name)
# # # print(student)

# # # square ={}
# # # for i in range(1,11):
# # #     square.update({i:i*i})

# # # print(square)

# # # find frequency of words

# # # f ={}

# # # word = list(input("Enter a sentence= ").split())
# # # for j in word:
# # #         if j in f:
# # #             f.update({[j] : f[j]+1})
# # #         else:
# # #             f.update({[j] : 1})
# # # print(f)   
    

# # f={}
# # word = list(input("Enter a sentence= ").lower().split())

# # for j in word:
       
# #         if j in f:
# #             f[j] = f[j]+1
# #         else:
# #             f[j] = 1
# # print(f)


# # def add(a ,b ):
# #     return a+b
# # result = add(5,7)
# # print(result)




# lst = [1,2,3,4,5]

# def lst1 (lst):
#  count=0
#  for i in lst:
#     count=count+1
#  return count
# ans = lst1(lst)



# def printList (lst):
#  count=0
#  for i in lst:
#     print(i,end="")
 
# def usd(a):
#   return a*90

# ans = usd(1)
# print(ans)
# # printList(lst)


# def factorial(a):
#    fact = 1
#    for i in range(1,a+1):
#        fact = fact * i
#    return fact



# def permutation(a,r):
#     n = factorial(a)
#     p = factorial(a-r)
#     per = n/p
#     return per


# def combination(a,r):
#     n = factorial(a)
#     p = factorial(r)
#     c=factorial(a-r)
#     rem = p*c
#     per = n / rem
#     return per


# ans = permutation(5,5)
# ans1 = combination(5,4)
# print(ans)
# print(ans1)



# for i in range(10):
#     print(i)
# s = {1,2,3,4}
# print(type(s))
# # print(len(s))

# def sum(n):
#     if (n==11):
#         return
#     print(n)
#     sum(n+1)



# def sum(n):
#     if (n==1):
#       return 1
#     sum1 = n * sum(n-1)
#     return sum1
# ans = sum(5)
# print( ans )




# n = int(input())
# s = set(map(int, input().split()))
# N = int(input())
# for i in range(N):
#     cmd =input().split()
#     if cmd[0]== "pop": 
#         # length = len(s)     
#         # if length > 0:
#           s.pop() 
#     elif cmd[0] == "remove":
#         x = int(cmd[1])
#         if x in s:
#           s.remove(x) 
#     elif cmd[0] == "discard":
#         s.discard(int(cmd[1]))    
# print(sum(s))

# s ={1,2,3,4,5}
# s.pop()
# print(s)
# s ={2,3,4,5}
# s.pop()
# print(s)

# line = int(input().split())
# n = int ( input())
# setA,setB = set(map(int(input().split())))

# print(setA)
# print(setB)

# Input: nums = [1, 2, 3, 1, 1, 1, 4, 2, 3], k = 6  
# Output: 3  
# Explanation: The longest subarray with sum 6 is [1, 1, 4] or [4, 2], both have length 3.

nums = [1, 2, 3, 1, 1, 1, 4, 2, 3]
k = 6

for i in range(len(nums)):
    for j in range(i+1):
        if i < 3 :
            print(nums[j])



