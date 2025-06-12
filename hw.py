#1
L=[10,45,1,67,56]#prints list
print(L)
L.sort()#ascending order using sort
print(L)
L=[10,45,1,67,56]
L.sort(reverse = True)#descending order use sort() and check reverse is true
print(L)
#2
x={"a","b","c","d"}
y={"a",1,"d",2}
z=x.intersection(y)#it will print the common ones
print(z)
z=x.symmetric_difference(y)#it will not print the common ones ie uncommon 
print(z)
x.remove("b")#it will remove that int using remove()
print(x)
#3
t=("Ria","sia","pia")#print tuple using() and ,
print(t)
L=list(t)
L.append("mia")#add elements in the last
print(L)
L.remove("pia")#remove string
print(L)
#4
t="     I could drive all day"
print(t)
print(len(t))#index value
print(t.replace("drive","drink"))#replace the given characters
print(t.lstrip())#remove spaces in beginning
