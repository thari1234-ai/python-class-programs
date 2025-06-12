#dictionary
d1=dict(pet="yash",veg="carrot",flower="lily")
print(d1)
print(d1.get("veg"))
k=d1.keys()# to display keys
print(k)
d1["colour"]="red"# add items
print(d1)
d1.pop("colour")# it will remove dictionarykey and value
print(d1)
d1.popitem()# it will remove last inserted item
print(d1)
for i in d1: # display keys in new line
    print(i)
for i in d1:# display values in new line
    print(d1[i])
for i in d1.values():
     print(i)
for i in d1.keys():
     print(i)
d2=dict(d1)
print(d2)
