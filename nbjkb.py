total_amt = int(input('Enter your initial amount: '))

while True:
    print('1. Deposit')
    print('2. Withdraw')
    print('3. View Balance')
    print('4. Exit')
    
    option = input('Enter your choice (1 to 4): ')

    match option:
        case '1':
            deposit_amt = int(input('Enter deposit amount: '))
            total_amt += deposit_amt
            print(f'Successfully deposited! Your balance is now {total_amt}.')
        case  '2':
            withdraw_amt = int(input('Enter withdrawal amount: '))
            total_amt -= withdraw_amt
            print(f'Successfully withdrawn! Your balance is now {total_amt}.')
       
        case '3':
            print(f'Your current balance is {total_amt}.')
        case '4':
            quit()
        
        case'_':
            print('Invalid option. Please choose a valid option (1 to 4).')
