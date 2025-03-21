#Swap value using 3rd variable

val1=input("Enter First Value - ")
val1=int(val1)

val2=input("Enter Second Value - ")
val2=int(val2)

# val3=val1
# val1=val2
# val2=val3
#
# print("After swap First value " + str(val1))
# print("After swap Second value " + str(val2))

#Swap value without using 3rd variable
val1=(val1+val2)-val1
val2=(val1+val2)-val2
print("After swap First value " + str(val1))
print("After swap Second value " + str(val2))