#set()
x={10,20,30,40}#set
print(x)
print("true" if 10 in x else "false")# it will print true if that int is preent else false
print(x)
x.add(50) #add elements in set
print(x)
for i in x: # for is used to print in next line
    print(i)
print(bool(90))#if it present and also it will print true for any numbers present it will return true else false for empty
print("true"if 10 in x else"false")
y={70,90,80,100}
x.update(y)
print(x)
x.remove(10)#it will remove that int using remove()
print(x)
x.discard(99)#it will print the set even if its doesnt have a error it wont show error and will remove()
print(x)
x.pop()# it will remove rendomly because it is unindexed
print(x)
x.clear()# it will clear the inputs inside
print(x)
x={10,20,30}
del(x)# delete the whole set()
s={10,20,30,40}
x={"a","b","c","d"}
y=s.union(x)#union to join to sets
print(y)
x={"a","b","c","d"}
y={"a",1,"d",2}
z=x.intersection(y)#it will print the common ones
print(z)
z=x.symmetric_difference(y)#it will not print the common ones 
print(z)
z=x.symmetric_difference_update(y) # it will update to the set and will return none
print(z)

