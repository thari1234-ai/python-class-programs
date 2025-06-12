total_amount=int(input("Enter the total amount:"))
while True:
  print("1.Deposit\nWithdraw\nView Balance\nExit")
choice = input("Enter choice (1/2/3/4): ")
amount=int(input("Enter the amount:"))
deposit=total_amount+amount
withdraw=total_amount-amount
balance=total_amount+deposit-withdraw
match choice:
    case'1':
        print(deposit)
    case'2':
        print(withdraw)
    case'3':
        print("Current balance:",total_amount)
        
    case'4':
        quit()
    case _:
        print("First learn how to access bank stuffs,idiot")
