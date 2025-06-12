# Get input from user
num = int(input("Enter a number: "))

# Check if number is valid
if num <= 0:
    print("Please enter a positive integer")
else:
    print(f"Factors of {num} are:", end=" ")
    # Loop to find factors
    for i in range(1, num + 1):
        if num % i == 0:
            print(i, end=" ")
