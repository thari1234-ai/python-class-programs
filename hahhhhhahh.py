#1
for x in range(8):
    print(x * 4, end=' ')
print()   
#2
   
row = int(input("Enter the number of rows: "))
col = int(input("Enter the number of columns: "))

for i in range(row):
    for j in range(col):
        print("&", end=" ")
    print()
#3
scores = [85, 90, -5, 76, 92, -1, 88, 79, 55]
for x in scores:
    if x == -1:
        print("Encountered missing data. Stopping processing")
        break
    elif x < 0:
        print(f"Invalid score {x} encountered. Skipping.")
        continue
    else:
        print(f"Score: {x}")
