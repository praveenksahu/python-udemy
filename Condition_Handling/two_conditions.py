#print a number is odd or even

data=input("Enter a Number:- ")
data=int(data)

if(data<0):
    print("Negative Number")
elif(data==0):
    print("Number is 0")
elif(data%2 == 0):
    print("Even Number")
else:
    print("Odd Number")