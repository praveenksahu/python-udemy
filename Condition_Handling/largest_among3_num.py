f_num = input("Enter the First Number: ")
f_num=int(f_num)

s_num = input("Enter the Second Number: ")
s_num=int(s_num)

t_num = input("Enter the Third Number: ")
t_num=int(t_num)

# if(f_num > s_num and f_num > t_num):
#     print("First Number is Greater: " + str(f_num))
#
# elif(s_num > t_num and t_num > f_num):
#      print("Second Number is Greater: " + str(s_num))
# else:
#      print("Third Number is Greater: " + str(t_num))

# Approch 2
if(f_num == s_num == t_num):
    print("All the three numbers are Equal")
else:
    if(f_num >= s_num):
        if(f_num >= t_num):
            print("Greater Number is: " + str(f_num))
        else:
            print("Greater Number is: " + str(t_num))
    elif(s_num >= t_num):
        print("Greater Number is: " + str(s_num))
    else:
        print("Greater Number is: " + str(t_num))