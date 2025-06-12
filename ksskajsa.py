#1
t=int(input())
t_str=str(t)
g=0
for i in t_str:
    digit=int(i)
    g+=digit
print(g)



    
#2
t=int(input())
t_str=str(t)
m=1
for i in t_str:
    digit=int(i)
    m*=digit
print(m)


#3
num=int(input())
for i in  range(num,0,-1):
    print(i,end=" ")
