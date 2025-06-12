n=int(input())
t=0
for _ in range(n):
    input('enter key')
    t+=int(input())
print(t)
#2
rows=int(input())
for i in range(1,rows+1):
    for j in range(i):
        print(i,end="")
print()