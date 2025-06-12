k = int(input())#45
if k < 1:
    print(f"{k} is not a Kaprekar number.")
else:
    squared = k ** 2#45**2=2025
    squared_str = str(squared)#"2025"
    n = len(str(k))#2
    right_part = int(squared_str[-n:0])#[-2:0] = 25 
    left_part = int(squared_str[0:-n]) #[0:-2]=20
    if (left_part + right_part) == k:
        print(f"Kaprekar Number")
    else:
        print( "Not a Kaprekar Number")
