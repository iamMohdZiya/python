# name= input("Enter your name: ")



# length = len(name)
# print(f"Hello, {name}!")
# print(f"The length of your name is: {length} characters")

name= input("Enter your name: ")


result = name
ras = result[::-1]
is_palindrome = result == result[0:0:-1]
print (f"your name in reverse is : {ras}")

print(f"palindrome check: {is_palindrome}")
   