import math
n=int(input())
first=int(n%10)
second=int(((n//10)%10))
third=int(n//10)
x=math.factorial(first)+math.factorial(second)+math.factorial(third)
print(x)
