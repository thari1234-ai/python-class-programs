total_amount = int(input("Enter the total amount: "))

while True:
    print("\nMenu:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. View Balance")
    print("4. Exit")
    
    choice = input("Enter choice (1/2/3/4): ")
    
    match choice:
        case '1':
            amount = int(input("Enter the amount to deposit: "))
            total_amount += amount
            print(f"Deposit of {amount} is successful. Current balance: {total_amount}")
        
        case '2':
            amount = int(input("Enter the amount to withdraw: "))
            total_amount -= amount
            print(f"Withdrawal of {amount} is successful. Current balance: {total_amount}")
        
        case '3':
            print(f"Current balance: {total_amount}")
        
        case '4':
            quit()
        
        case _:
            print("Invalid choice")
