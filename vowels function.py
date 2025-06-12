s=list(map(int,input().split()))
u=[]
for i in s:
    if i not in u:
        u.append(i)
    elif i in u:
        u.remove(i)
print(u)

    
    

