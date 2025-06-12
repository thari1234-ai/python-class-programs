balance = float(input("Enter initial balance: "))  # Initial balance as input

while True:
    print("\nMenu:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. View Balance")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    match choice:
        case '1':
            amount = float(input("Enter amount to deposit: "))
            if amount > 0:
                balance += amount
                print(f"Successfully deposited {amount}. Current balance: {balance}")
            else:
                print("Deposit amount should be positive.")
        
        case '2':
            amount = float(input("Enter amount to withdraw: "))
            if 0 < amount <= balance:
                balance -= amount
                print(f"Successfully withdrew {amount}. Current balance: {balance}")
            else:
                print("Invalid withdrawal amount. Please check your balance.")
        
        case '3':
            print(f"Current balance: {balance}")
        
        case '4':
            quit()
        
        case _:
            print("Invalid choice")
