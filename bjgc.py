# Get input string from user
x = input("Enter a string: ")

# Convert the string to uppercase
x= input_string.upper()

# Initialize an empty string to store the reversed string
reversed_string = ""

# Initialize index to the last character of input_string
index = len(x) - 1

# Loop while index is greater than or equal to 0
while index >= 0:
    # Append character at current index to reversed_string
    reversed_string += x[index]
    # Decrement index to move to the previous character
    index -= 1

# Display the reversed string
print("Reversed string:", reversed_string)
