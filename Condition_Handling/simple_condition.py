#print a number is odd or even

data=input("Enter a number greater then 0: ")
data=int(data)
if(data % 2 == 0):
    print(str(data) + " - is a Even Number")

print(str(data) + " - is a Odd Number")