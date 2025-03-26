#Define Dictionary

dict={1:"one",2:"Dict", "key1":10,1:"New"}
print(dict)
print(len(dict))
print(dict[1])

#Print only keys
print(dict.keys())

#Print only values
print(dict.values())

#Add new value
dict["a"]="New val"
print(dict.values())

#Update value
dict["a"]="New"
print(dict.values())

#Delete items
dict.pop(1)
print(dict.values())

