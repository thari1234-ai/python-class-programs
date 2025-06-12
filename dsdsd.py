# Get input from user for N
N = int(input("Enter the value of N: "))

# Initialize the first two Fibonacci numbers
a, b = 0, 1

# Check if N is a valid number
if N <= 0:
    print("Please enter a positive integer")
elif N == 1:
    print("Fibonacci series:", a)
else:
    print("Fibonacci series:", end=" ")
    # Loop to print the Fibonacci sequence
    for _ in range(N):
        print(a, end=" ")
        a, b = b, a + b
