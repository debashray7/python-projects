print('''===== ATM MACHINE =====
1. Check Balance
2. Deposit
3. Withdraw
4. Transaction History
5. Exit
========================''')
current_balance = 10000.00
net_deposit = 0.0
net_withdrawal = 0.0
history = []
while True:
    try:
        choice = int(input('\nChoice: '))
    except ValueError:
        print('❌ Invalid Input!')
    else:
        if choice == 1:
            print(f'💰 Current Balance: ₹{current_balance}')
        elif choice == 2:
            try:
                deposit = float(input('Enter deposit amount: ₹'))
                if deposit <= 0:
                    print('❌ Deposit amount must be positive!')
                    continue
            except ValueError:
                print('❌ Invalid Input!')
            else:
                current_balance += deposit
                net_deposit += deposit
                history.append(deposit)
                print(f'✅ Deposited ₹{deposit}')
                print(f'💰 Available Balance: ₹{current_balance}')
        elif choice == 3:
            try:
                withdrawal = float(input('Enter withdrawal amount: ₹'))
                if withdrawal <= 0:
                    print('❌ Deposit amount must be positive!')
                    continue
                elif (current_balance - withdrawal) < 5000.00:
                    print('❌ Transaction declined.')
                    print(f'💡 You can withdraw upto {current_balance - 5000.00}')
            except ValueError:
                print('❌ Invalid Input!')
            else:
                current_balance -= withdrawal
                net_withdrawal += withdrawal
                history.append(-withdrawal)
                print(f'✅ Withdrawn ₹{withdrawal}')
                print(f'💰 Available Balance: ₹{current_balance}')
        elif choice == 4:
            print('===== TRANSACTION HISTORY =====')
            for i in range(len(history)):
                if history[i] > 0:
                    print(f'{i + 1}. Cr: ₹{history[i]}')
                else:
                    print(f'{i + 1}. Dr: ₹{abs(history[i])}')
            print('================================')
            print(f'1. Deposit: +₹{net_deposit}')
            print(f'2. Withdrawal: -₹{net_withdrawal}')
            print(f'💰 Available Balance: ₹{current_balance}')
            print('================================')
        elif choice == 5:
            print(f'💰 Final Balance: ₹{current_balance}')
            print('\n👋 Thank you for using ATM!')
            break
        else:
            print('❌ Invalid Input!')