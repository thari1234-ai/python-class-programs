# 5. Check for Balanced Array
# Given an array, check whether the sum of elements on the left is equal to the sum of elements on the right at any index.

# Example:
# arr = [1, 2, 3, 4, 10, 1, 2, 3]
# Output: True

arr = list(map(int, input("Enter the numbers separated by spaces: ").split()))
for i in range(1, len(arr)):
    left_sum = sum(arr[:i])
    right_sum = sum(arr[i:])
    if left_sum == right_sum:
        print("Balanced array found at index", i)
        break
else:
    print("No balanced array found")