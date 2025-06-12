# Get input string from the user
x = input("Enter a string: ")

# Convert the string to uppercase
x_upper = x.upper()

# Initialize an empty string for the reversed string
reversed_string = ""

# Iterate over the indices of the string in reverse order
for i in range(len(x_upper) - 1, -1, -1):
    reversed_string += x_upper[i]

# Print the reversed string
print("Reversed string:", reversed_string)
