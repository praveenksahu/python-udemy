#Loop List items
plang=['C', 'C++', 'Python', True, False, 'Jira', 'Java', 10, 'STL', 11]

for i in plang:
    print(i)

list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for slist in list_of_lists:
    for s in slist:
        print(s,end=" ")
    print()

print(type(list_of_lists)) #<class 'list'>