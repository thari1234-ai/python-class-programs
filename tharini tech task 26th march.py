flowerbed = list(map(int, input("Enter flowerbed (space-separated 0s and 1s): ").split()))
n = int(input("Enter number of flowers to plant: "))

flowerbed = [0] + flowerbed + [0]  # Add padding
count = 0

for i in range(1, len(flowerbed) - 1):
    if flowerbed[i - 1] == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
        flowerbed[i] = 1
        count += 1
        if count >= n:
            print(True)
            break
else:
    print(False)