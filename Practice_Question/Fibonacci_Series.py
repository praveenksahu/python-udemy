#Fibonacci Series
#0,1,1,2,3,5,8,13,21

x=input("Enter the Number to generate Fibonacci series: ")
x=int(x)

a=0
b=1
print(a,end=" ")
print(b,end=" ")
while((a+b)<x):
    b=a+b
    a=b-a
    print(b,end=" ")


