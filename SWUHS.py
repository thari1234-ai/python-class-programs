N1 = int(input("Enter number of rows (N1): "))#rows #5
N2 = int(input("Enter number of columns (N2): "))#col #5 
for i in range(N1):#row concentrate#0,1,2,3,4
    for j in range(N2):#col0,1,2,3,4
        if i == 0  or j == 0 :#
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()  # Move to the next line after each row

