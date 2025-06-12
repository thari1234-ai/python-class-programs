while True:# to repeat from 1st after 4digit
    t = input("Enter a 3-digit number: ")
    
    if len(t) != 3:
        print("3digit only")
        continue  # Restart the loop to prompt the user again
    
    first = int(t[0])
    second = int(t[1])
    third = int(t[2])
    powers = len(t)
    
    sum_of_cubes = first**powers + second**powers + third**powers
    g= int(t)
    
    if sum_of_cubes == g:
        print(f"{g} is an Armstrong number.")
    else:
        print(f"{g} is not an Armstrong number.")
    
    break  # Exit the loop since a valid input has been processed
