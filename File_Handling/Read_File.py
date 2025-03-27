
file = open ('cmd.txt')
# # #print("***********1************")
# # # print(file.readline())
# # # print(file.readline())
# # # print(file.read(10))
# # print("***********2************")
# # line=file.readline()
# # while line != "":
# #     print(line)
# #     line=file.readline()

print("***********3************")
num=1
list1=file.readlines()
for i in list1:
    if num <= 10:
        print(i)
    num+=1
file.close()