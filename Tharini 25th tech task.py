candies = list(map(int, input("Enter candies list: ").split()))
extraCandies = int(input("Enter extra candies: "))

max_candies = max(candies)
result = [(candy + extraCandies) >= max_candies for candy in candies]

print(result)