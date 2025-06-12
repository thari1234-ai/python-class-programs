print("Odd numbers:", end=' ')
for x in range(1, 11):
    if x % 2 != 0:
        print(x, end=' ')
print()

print("Even numbers:", end=' ')
for x in range(1, 11):
    if x % 2 == 0:
        print(x, end=' ')
print()
#2
# Prompt user for input
sales_figures = input("Enter sales figures separated by spaces: ")

# Convert input string to list of integers
sales_figures = list(map(int, sales_figures.split()))

# Initialize counters
successful_count = 0
returns_losses_count = 0

# Iterate through the list
for number in sales_figures:
    if number > 0:
        successful_count += 1
    elif number < 0:
        returns_losses_count += 1

# Output the results
print("Number of successful sales:", successful_count)
print("Number of returns or losses:", returns_losses_count)
