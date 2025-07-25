
# practical for string operations
# string operations
a = "  Hello, World!"

print("Slicing : "+ a[2:5])
print("In UpperCase :"+ a.upper()) 
print("Length of the String:",len(a)) 
print("Reversed String:" + a[::-1])
print("In LowerCase :"+ a.lower()) 
print("In TitleCase :"+ a.title()) 
print("In Capitalized Case :"+ a.capitalize())  
print("In SwapCase :"+ a.swapcase())  
print("Index of 'World' : " + str(a.index("World")))
print("Count of 'o' " + str(a.count("o")))
print(" start with 'Hello'? " + str(a.startswith("Hello")))
print(" end with '!'? " + str(a.endswith("!")))
print("split:" , a.split(" "))
print("Strip: ", a.strip())
print("Trim:"+a.rstrip())
print("Trim :"+a.lstrip())
b = " Yooo!"

print("Concatenated String: " + a + b)



