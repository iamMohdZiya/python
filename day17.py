





# if sorted(a)==sorted(b):
#     print("True")
# else:
#     print("False")


# for i in range(n):
#     for j in range(n2):
#         if a[i]==a[j]:




# a = "hello"
# b = "olleh"
# n = len(a)
# n2 = len(b)
# count = 0
# if n ==n2:
#         for i in range(n):
#             # for j in range(n2):
#             if a[i] in b:
#                 # if a[i] == b[j]:
#                 count = count+ 1
#         if count == n:
#             print("True")
#         else:
#             print("False")
# else:
#     print("False")



# year = 1999
# leap = False
# if (year%4==0):
#     if(year%10==0):
#         if(year%400==0):
# #             leap = True
# #         else:
# #             leap=False
# #     else:
# #         leap=True
# # else:
# #         leap=False
# # print( leap)





# str1 = "abkardabra"
# l1 = list(str1)
# n = len(l1)
# dect = {}

# for i in range(n):
#    if l1[i] in dect:
#        dect[l1[i]] += 1
#    else:
#        dect[l1[i]] = 1
# print(dect)

# # three sum
# if __name__ == '__main__':
#     n = int(input())

#     students = []

#     for _ in range(n):
#         name = input()
#         grade = float(input())
#         students.append([name, grade])

#     grades = sorted(set([student[1] for student in students]))

#     second_lowest = grades[1]

#     second_lowest_students = [student[0] for student in students if student[1] == second_lowest]

#     second_lowest_students.sort()

#     for name in second_lowest_students:
#         print(name)

# # a = [1,2,3,4,5]
# # target =12
# d = set()
# n = len(a)
# for i in range(n):
#     for j in range(1,n):
#         for z in range(2,n):
#             if a[i]+a[j]+a[z] == target:
#                 d.add(i)
#                 d.add(j)
#                 d.add(z)


# s = []
# n = int(input())

# for _ in range(n):
#         name = input()
#         grade = float(input())
#         s.append([name, grade])


# grades = []
# for student in s:
#     grades.append(student[1])

# grades = list(set(grades))  

# s0 = grades[0]

# s2 = []
# for student in s:
#     if student[1] == s0:
#         s2.append(student[0])

# s2 = list(set(s2))  

# s2.sort()
# for name in s2:
#         print(name)


# x =10 

# def bar():
#     print(x)
#     x = 20
# bar()


# print(sum(range(5),start=10))
# print("123"==['1','2','3'])

# name = "developer"
# print(name[::-1])

# text = "python"
# # print(text[1:3])

# # numbers= [2, 3, 4, 5, 6, 7, 8, 9, 10]

# # numbers[2:4]=[3,7]
# # print(numbers)

# print([] is [])
# print(() is ())
# print('' is '')


# a = print("hello")
# print(a)

# n = 5 
# for i in range(n):
#     for j in range(1, i*2 + 2):
#         print("1", end="")
#     print()


# n = 5
# for i in range(n):
#     for space in range(n-i):
#         print(" ",end="")
#     for star in range(1,i*2):
#         print("*",end="")
#     print()


nums = [1,2,0]
# for i in range(1,len(a)):
#     if i not in a:
#         print(i)
#         break

def firstMissingPositive( nums ):
        num = None
        nums.sort()
        print(nums)
        for i in range(len(nums)+1):
            if i not in nums:
                num = i
                print("he")
        print("Hello")
        return num
a = firstMissingPositive(nums)
print(a)