#Triangle is EQUILATERAL|SCALENE|ISOSCELES

s1=input("Enter side one: ")
s1=int(s1)

s2=input("Enter side two: ")
s2=int(s2)

s3=input("Enter side three: ")
s3=int(s3)

if(s1==s2 and s1==s3):
    print("EQUILATERAL Triangle")
elif(s1==s2 or s2==s3 or s1==s3):
    print("ISOSCELES Triangle")
else:
    print("SCALENE Triangle")