num1=input("Enter First number: ")
num1=int(num1)
num2=input("Enter Second number: ")
num2=int(num2)
num3=input("Enter Third number: ")
num3=int(num3)

if (num1<=num2 and num1<=num3):
    print("Smallest Number is: " + str(num1))
elif(num2<=num1 and num2<=num3):
    print("Smallest Number is: " + str(num2))
else:
    print("Smallest Number is: " + str(num3))