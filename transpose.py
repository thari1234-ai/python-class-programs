rows=int(input())
cols=int(input())
matrix=[]
for i in range(rows):
    row=list(map(int,input(f'enter row {i+1}:').split()))
    matrix.append(row)
transpose=[[matrix[j][i] for j in range(rows)] for i in range(cols)]
for row in matrix:
    print(" ".join(map(str, row)))
for row in transpose:
    print(" ".join(map(str, row)))