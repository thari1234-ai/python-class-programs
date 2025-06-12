r1, c1 = map(int, input().split())  # Rows and cols of first matrix
r2, c2 = map(int, input().split())  # Rows and cols of second matrix

if c1 != r2:  # Check if multiplication is possible
    print("Matrix multiplication is not possible")
else:
    A = [list(map(int, input().split())) for _ in range(r1)]  # First matrix
    B = [list(map(int, input().split())) for _ in range(r2)]  # Second matrix

    # Multiply matrices and print result
    for i in range(r1):
        print(*[sum(A[i][k] * B[k][j] for k in range(c1)) for j in range(c2)])
