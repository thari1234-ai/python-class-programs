#1
n = int(input())#234=9
sum_digits = 0
while n > 0:
    last = n % 10#234%10=4,3
    sum_digits += last#4,3
    n//= 10#23
print( sum_digits)
#2
n = int(input("Enter a positive integer: "))

product_digits = 1


current_number = n
while current_number > 0:

    digit = current_number % 10
    

    product_digits *= digit
    

    current_number //= 10
print("Product of digits of", n, "is", product_digits)

#3
# Input number
n = int(input())#8
for i in range(n, 0, -1):
    print(i, end=" ")  

print()
