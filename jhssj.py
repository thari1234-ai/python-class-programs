k = int(input().strip())  # Read input and convert to integer

k_squared = k * k  # Calculate k squared
k_squared_str = str(k_squared)  # Convert k squared to string for manipulation

is_kaprekar = int(k_squared_str[:i]) + int(k_squared_str[i:]) == k
for i in range(1, len(k_squared_str)):
    print(f"{k} is {'a Kaprekar number' if is_kaprekar else 'not a Kaprekar number'}")
