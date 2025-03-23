#String in Python

#Normal String
s1="Test"
s2="Hello World"
print(s1, s2)

#multiple line string
multipleline='''
Hello to 
the world
of Python
'''
print(multipleline)

multiline=""""
test
multiline
output"""
print(multiline)

#String Indexing
str="TeSting for LearninG"
print (str[2]) #print 3rd char S
print (str[-1]) #print last character G
print(str[0]) #print first character T

#String Slicing
str1="0123456789 10"

print(str1[::]) #0123456789 10

print(str1[::-1]) #01 9876543210

print(str1[1:5]) #1234

print(str1[1:10:2]) #13579

#String Immutability
str2=" ello World of Python"
str2="H" + str2[1:]
print(str2) #Hello World of Python

#Replace with other string

s5="hello world"
print(s5) #hello world
s5="H" + s5[1:]
print(s5) #Hello world
s6=s5.replace("world", "World")
print(s6) #Hello World

