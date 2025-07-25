# from collections import deque
# d = deque()
# d.append(18)
# d.append(29)

# # print(f"{d}")
# # d.pop()
# # print(f"{d}")


# from collections import deque
# n = input("Enter a word : ")

# d = deque(n)

# flag = False
# print(d)
# print(len(d))
# while(len(d)>1):
#     if d.pop() != d.popleft():
#         flag = False
#     else:
#         flag = True
# if flag == True :
#     print("its a palindrome ")
# else:
#     print("Not a pal")

# binary tree 

# a = [1,23,4,3,7,1,4,6]
# target = 10 
# s = set()
# n =len(a)
# for i in range(n):
#     for j in range(1,n):
#         if a[i]+a[j] == target:
#             s.add(a[i])
#             s.add(a[j])
# print(s)


# number =-1344
# flag = False
# print(number)
# if -number:
#     number = -1 * number
#     flag=True
# print(number)
# temp = number
# re = 0
# while temp > 0:
#     r = temp % 10 
#     re = re *10 + r
#     temp = temp // 10
# if flag ==True:
#     re = -1 * re
# print(re)



# class node:
#     def __init__(self,rootnode,left= None ,right= None):
#         self.left = left
#         self.right= right
#         self.rootnode= rootnode


# root = node (2)
# root.right=node(43)
# root.left=node(43)

# root.right.right=node(43)
# root.right.left=node(33)

# root.left.left=node(90)
# root.left.right=node(77)

# def display(node):
#     if node:
#         print(node.rootnode,end=" ")
#         display(node.left)
#         display(node.right)
# def post(node):
#     if node:
#         post(node.left)
#         post(node.right)
#         print(node.rootnode,end=" ")
# def inOrder(node):
#     if node:
#         inOrder(node.left)
#         print(node.rootnode,end=" ")
#         inOrder(node.right)

# print("pre order")
# display(root)

# print()
# print("post order")

# post(root)
# print()


# print("In order")

# inOrder(root)
# print()





