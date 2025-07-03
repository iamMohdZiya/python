import random
import string as str

passWord = str.ascii_letters + str.digits + str.punctuation
ran = ""
n= int(input("Enter length of Password: "))
for i  in range(n+1):
     ran = ran + random.choice(passWord)

print(f"Your password is {ran}")