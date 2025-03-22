#Prime Number or Not

num=input("Enter a number: ")
num=int(num)

x=2
for i in range (x,num):
    if(num % i == 0):
        print("Not a Prime Number")
        i+=1
        break
else:
    print("Prime Number")
