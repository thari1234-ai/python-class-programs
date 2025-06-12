arr=list(map(int,input("sperate input by space:").split()))
n=len(arr)+1
total=n*(n+1)//2#4*5//2
#10
arr_s=sum(arr)
missing=total-arr_s#total-sum of the array
print("missing",missing)

