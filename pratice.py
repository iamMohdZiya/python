  
# a  = [1,2,3,4,6]
# b = [1,2,3,4,5,6,7,8,9]
# n =len(a)
# for i in range(n-1):



# print peramid 1 
# 
#   1
#  121
#  12321
#  1234321

# n = 4

# for i in range(1,n):
#     # for space in range(n-i,0,-1):
#     #     print(" ",end="")
#     for star in range(1-i,n,3):
#         print(i)

# n = 4
# for i in range(1, n+1):
#     print(" " * (n - i), end="")
#     for j in range(1, i + 1):
#         print(j, end="")
#     for j in range(i - 1, 0, -1):
#         print(j, end="")
#     print()


# # find frequency of each character in a string
# s = "hello"
# f = {}

# for i in s:
#     f[i] = f.get(i, 0) + 1  #

# print(f)

# sentence = "hello yyworld"

# words = sentence.split()

# longest_word = max(words, key=len)

# print(f"The longest word is: {longest_word}")
   
    





# # reverse
# # a = [2,4,3,5,3,4,5,4,5,1]
# a = [3,56,3,35,43,343222,6,33,0]

# min = a[0]
# max = a[0]

# for num in a:
#     if num > max:
#         max = num
#     elif num < min :
#         min = num 
# print(max)
# print(min)

# s1 = "madam"
# rev = s1[::-1]
# print(rev==s1)

# Count Vowels and Consonants in a String
# Input: "Ziya" → Output: Vowels = 2, Consonants = 2

# vo = [ "a","e","i","o","u"]
# str1 = "ziya"
# l1 = list(map(str,str1))
# print(l1)
# con = 0 
# vol = 0 
# for i in range(len(l1)):
#     if l1[i] in vo:
#         vol = vol + 1
#     else:
#         con = con + 1
# print(vol)
# print(con)



# Move All Zeroes to End
# Input: [0,1,0,3,12] → Output: [1,3,12,0,0]
 

# a = [1, 3, 3, 0, 5, 34, 3, 0]

# result = [num for num in a if num != 0]  # All non-zero elements
# result = result + [0] * (len(a) - len(result))   # Add zeroes at the end

# print(result)

# a = [1,1,2,2,3,3]
# # s = set(a)
# # a = list(s)
# # print(a) 


# s = "aabbccddeefg"
# dec= {}
# for char in s:
#     dec[char] = dec.get(char,0)+1 

# for char in s:
# #     if dec[char]==1:
# #         print(char)
# #         break
       

# a = [1, 2, 3, 4, 5]

# D = 2

# rot = a[D:] + a[:D]

# print(rot)

# a = [1,2,4,5,6]
# n = max(a)
# for i in range(1,n+1):
#     if i not in a:
#         print(i)
#         break

# string1 = "hello"

# # sub ="ello"
# # flag = False
# # for i in range(len(string1)- len(sub)+1):
# #     if string1[i:i+len(sub)]==sub:
# #         flag= True
# #         break
# # print(flag)

def count(s):
    l1=list(map(str,s))
    vowel=["a","e","i","o","u"]
    count=0
    for num in l1:
        if num in vowel:
            count=count+1
    return count


def max(l):
   max= l[0]
   for num in l:
       if num > max:
           max = num
    
   return max

s = "sucess"
f={}

for num in s:
    f[num]=f.get(num,0)+1
for num in s:
    if f[num]==1:
        print(num)
        break

