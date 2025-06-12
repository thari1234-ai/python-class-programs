def power(x,n):
    if n==0:
        return 1
    elif n>0:
        return x*power(x,n-1)
    else:
        return 1/power(x,-n)
result=power(2,-1)
print(result)