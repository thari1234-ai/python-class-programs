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
