#Factorial of a number
#5= 5*4*3*2*1

number=input("Enter a number to find Factorial: ")
prt=number
number=int(number)

fact=1
while(number>0):
    fact=fact*number
    number-=1
print("Factorial of " + prt +" is " + str(fact))