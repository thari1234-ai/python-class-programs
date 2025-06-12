t=()
print(t)#empty tuple
t=("thari","poori")
print(t)
print(len(t))#to check its length
t1=(10)
print(t1)#it wont print as tuple as it has only 1
t2=(10,)
print(t2)#it prints as a tuple
L=list(t)#  converts tuple into list
L.append("soori")# adds element at the end
print(L)
t=tuple(L)#coverts list into tuple
print(t)
t=("thari")
g=("goose")
t+=g#to add tuples
print(t)
