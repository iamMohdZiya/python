# # # num1 = int(input("Enter a number="))

# # # num2 = int(input("enter a 2nd number="))

# # # num3=int(input("enter a 3rd number="))

# # # if num1>num2 and num1>num3:

# # #   print(f"greater number is {num1} ")
# # # elif num2>num3 :
# # #   print(f"greater number is {num2}")
# # # else :
# # #   print(f"greater number is {num3} ")
# # # ans = max(num1,num2,num3)
# # # print("f{ans}") 


# # num1 = int(input("Enter a number="))


# # result =  "is multiple of 7" if num1 % 7 ==0 else "not multiple of 7"
# # print(f"{num1}  {result}")


# # #  split and join by - 
# # text = input("Enter a sentence: ")
# # words = text.split()
# # joined_text = '-'.join(words)

# for i in range(100):
#   print(100-i)

# a = int(input("Enter a number="))
# for i in range(1,11):
#   print(f"{a}x{i}=",a*i)
# a = int(input("Enter a number="))
# i=1
# sum=0
# while(i<= a):
#     sum=sum+i
#     i=i+1
# print(f"Sum of numbers {sum}")

#factolrial of number

# a = int(input("Enter a number="))
# fac=1
# i=1
# while(i<= a):
#      fac=fac*i
#      i=i+1
# print(f"Factorial is {fac}")
# take input of three movies put them iin the list 
# str1 = input("Enter a Movie name =")
# str2 = input("Enter a Movie name =")
# str3= input("Enter a Movie name =")
loc = int(input("size="))
arr = map(loc, input().split())



for i in arr:
    print(i)