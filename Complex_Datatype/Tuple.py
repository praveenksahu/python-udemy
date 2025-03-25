#List - Only read is possible
#Allows Duplicate valued

tou=("list","touple", True,False)
print(tou) #('list', 'touple', True, False)

print(tou) #('list', 'touple', True, False)
print(tou[2]) #True
print(tou[1:]) #('touple', True, False)
print(tou[::-1]) #(False, True, 'touple', 'list')

for i in tou:
    print(i)

#Tuples don't support item assignment
#tou[2]="Touple"

