r1,c1=map(int,input().split())
A=[list(map(int,input().split())) for _ in range(r1)]
r2,c2=map(int,input().split())
B=[list(map(int,input().split())) for _ in range(r2)]
if c1 != r2:
    print("matrix multi is not applicable")
else:
    result=[[0]*c2 for _ in range(r1)]
    
    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                result[i][j]+=A[i][k]*B[k][j]
for row in result:
    print(*row)