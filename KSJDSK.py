input_number=int(input())
product_digits = 1  # Convert number to string to iterate over each digit
str_n = str(input_number)
for digit in str_n:
    product_digits *= int(digit)
print(product_digits)
