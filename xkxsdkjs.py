N1 = int(input("Enter number of rows (N1): "))#rows #5
N2 = int(input("Enter number of columns (N2): "))#col #5 
for i in range(N1):#row concentrate#1,2,3,4,5
    for j in range(N2):#col1,2,3,4,5
        if i == 0 or i == N1 - 1 or j == 0 or j == N2 - 1:#1st row 1st col last row last coloumn=1
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()  # Move to the next line after each row

