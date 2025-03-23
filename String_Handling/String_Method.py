#String Methods

str="Hello World of Python"
print(len(str)) #21

print(str.upper()) #HELLO WORLD OF PYTHON
print(str.lower()) #hello world of python

str1="   H e l l o   "
print (str1.strip()) #H e l l o

print (str1.lstrip()) #H e l l o
print (str1.rstrip()) #   H e l l o

#Concat
print(str + str1) #Hello World of Python   H e l l o

#Repeat
print(str1.strip() * 3) #H e l l oH e l l oH e l l o

#Formatting Strings
name="Vishal"
age=13
grade=9
print(f"Name: {name} , Age: {age} , Grade: {grade}") #Name: Aarya , Age: 13 , Grade: 9
# #Name: Vishal , Age: 13 , Grade: 9

fs= "My Name is {} , my Age is {} , and I study in Grade {}.".format("Vaishali",6,1)
print(fs) #My Name is Vaishali , my Age is 6 , and I study in Grade 1.

#substring is present in a string.
str2="Hello how are you"
print("H" in str2) #True
print("Z" in str2) #False