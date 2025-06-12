def sum_(n):
    if n==0:
        return 0
    return n%10+sum_(n//10)
result=sum_(1234)
print(result)