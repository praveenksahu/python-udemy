#List - read write is possible
#Allows Duplicate valued

plang=["Java", "C++", "Python", True,False]
print(plang) #['Java', 'C++', 'Python', True, False]
print(plang[2]) #Python
print(plang[1:]) #['C++', 'Python', True, False]
print(plang[::-1]) #[False, True, 'Python', 'C++', 'Java']

#Length
print(len(plang)) #5
plang[5:6]="C#","Java"
print(plang)

#Modify
plang[5]="Jira"
print(plang)

#Append
plang.append(10)
print(plang) #['Java', 'C++', 'Python', True, False, 'Jira', 'Java', 10]

#Insert
plang.insert(0,"C")
print(plang)#['C', 'Java', 'C++', 'Python', True, False, 'Jira', 'Java', 10]

plang.extend(["STL",11])
print(plang)#['C', 'Java', 'C++', 'Python', True, False, 'Jira', 'Java', 10, 'STL', 11]

#Remove first occurance
plang.remove("Java")
print(plang)#['C', 'C++', 'Python', True, False, 'Jira', 'Java', 10, 'STL', 11]

#Pppped
pop=plang.pop()
print("Popped Element: ",pop)#Popped Element:  11
print(plang)#['C', 'C++', 'Python', True, False, 'Jira', 'Java', 10, 'STL']

#Delete
del plang[7]
print(plang) #['C', 'C++', 'Python', True, False, 'Jira', 'Java', 'STL']
