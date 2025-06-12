n = int(input())
last = n % 10
first= n // 100
second = (n // 10) % 10
if first>last and first>second:
    print("1st")
elif last>first and last>second:
    print("2")
else:
     print("3 ") 
