#to check the num is perfect square##1
num = int(input("Enter a number: "))

if num < 0:
    print(f"{num} is not a Perfect Square")
else:
    root = 0#
    while root * root <= num:#0<4
        if root * root == num:
            print(f"{num} is a Perfect Square")
            break
        root += 1
    else:
        print(f"{num} is not a Perfect Square")
##2
n = int(input())#6
for i in range(1, n + 1):#1,7=1,2,3,4,5,6 upper 
    line = '*'.join([str(i)] * i)
    print(line)
for i in range(n, 0, -1):#6,5,4,2,1
    line = '*'.join([str(i)] * i)
    print(line)
##3
N1 = int(input("Enter number of rows (N1): "))#rows #5
N2 = int(input("Enter number of columns (N2): "))#col #5 
for i in range(N1):#row concentrate#0,1,2,3,4
    for j in range(N2):#col0,1,2,3,4
        if i == 0 or i == N1 - 1 or j == 0 or j == N2 - 1:#N1-1=LAST ROW,N2-1=LAST COLOUMN
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()  # Move to the next line after each row



