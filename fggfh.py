# factors find
num=int(input())
for i in range(1,num+1):
    if num%i==0:
        print(i,end=" ")
#2
n=int(input())
if n<2:
    f= False
else:
    f=True
    for i in range(2,n):
        if n%i==0:
            f=False
            break
if f:
       print("prime")
else:
     print("not prime")
        
