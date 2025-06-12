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
n = int(input("Enter a positive integer: "))

for i in range(n, 0, -1):
    print(i, end=" ")  # Print each number followed by a space

print()

