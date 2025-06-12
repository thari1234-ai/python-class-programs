n = int(input())#6
for i in range(1, n + 1):#1,7=1,2,3,4,5,6 upper 
    line = '*'.join([str(i)] * i)
    print(line)
for i in range(n, 0, -1):#6,5,4,2,1
    line = '*'.join([str(i)] * i)
    print(line)
