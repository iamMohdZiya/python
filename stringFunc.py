# name = input("enter name: ")
# end = name.endswith(".com")
# count = name.find("@")

# if end and count != -1:
#     print("The name is a valid email address.")
# else:
#     print("The name is not a valid email address.")
# # if name == name.upper():
# #     print("The name is in uppercase.")
# # elif name == name.lower():
# #     print("The name is in lowercase.")  
# # else:
# #     print("The name is in mixed case.") 

# if (number % 2 == 0):
#     print("The number is even.")
# else:   
#     print("The number is odd.")

name =input("Enter your username: ")

if (name.find(" ")!=-1):
    print("invalid username")
elif( len(name)<4):
    print("too short")
else:
    print("valid")

    
