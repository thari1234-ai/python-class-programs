print("THAR BANK WELCOMES YOU")
total_amount = int(input("Enter the total amount: "))  #1000
while True:
    print("\nMenu:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. View Balance")
    print("4. Exit")
    
    choice = input("Enter choice (1/2/3/4): ")
    
    match choice:
        case '1':
            amount = int(input("Enter the amount to deposit: "))#1000
            total_amount += amount#1000+1000
            print(f"Deposit of {amount} is successful. Current balance: {total_amount}")#2000
        
        case '2':
            amount = int(input("Enter the amount to withdraw: "))#1000
            total_amount -= amount#2000-1000
            print(f"Withdrawal of {amount} is successful. Current balance: {total_amount}")
        
        case '3':
            print(f"Current balance: {total_amount}")
        
        case '4':
            quit()
        
        case _:
            print("Invalid choice")
#2
print("THAR HOTEL WELCOMES YOU")
option = input("Enter your choice (1/2/3/4): ")
 
match option:
    case '1':
        print("\n tiffin Menu:")
        print("1. idly----------$90")
        print("2. dosa---------$1000")
        print("3. poori-----------$80")
 
    case '2':
        print("\n rice:")
        print("1. lemon rice---------$45")
        print("2. tomato rice--------$25")
        print("3. fried Rice---------$30")
 
    case '3':
        print("\n dessert Menu:")
        print("1. tiramisu---------$10")
        print("2. choco lava cake--------$25")
        print("3. icecreamuh----------$30")
 
    case '4':
              quit()
 
    case _:
              print("sorry,we dont have that food")



