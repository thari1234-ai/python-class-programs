print("HOTEL THAR WELCOMES YOU")
while True:
    print("\nMenu:")
    print("1. tiffin")
    print("2. rice")
    print("3. Dessert")
    print("4. Exit")
    
    option = input("Enter your choice (1/2/3/4): ")
    
    match option:
        case '1':
            print("\n tiffin Menu:")
            print("1. idly")
            print("2. dosa")
            print("3. poori")
        
        case '2':
            print("\n rice:")
            print("1. lemon rice")
            print("2. tomato rice")
            print("3. fried Rice")
        
        case '3':
            print("\n dessert Menu:")
            print("1. tiramisu")
            print("2. choco lava cake")
            print("3. icecreamuh:(")
        
        case '4':
            quit()
        
        case _:
            print("sorry,we dont have that food")
