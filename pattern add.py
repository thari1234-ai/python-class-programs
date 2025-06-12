n = 5

for i in range(1, n + 1):
    num = i
    for j in range(i):
        print(num, end=" ")
        num += (n - j - 1)  # Directly add decreasing values
    print()
