history = []
print('''===== CALCULATOR MENU =====
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Modulus
6. Power
7. Square Root
8. Show History
9. Exit
===========================
''')
while True:
    try:
        user = int(input('\nChoose operation (1-9): '))
    except ValueError:
        print('\n❌ Invalid Input!')
        input('\nPress ENTER to continue...\n')
        continue
    else:
        if user in [1,2,3,4,5,6]:
            try:
                n1 = float(input('\nEnter first number: '))
                n2 = float(input('Enter second number: '))
            except ValueError:
                print('\n❌ Invalid Input!')
            else:
                if user == 1:
                    print(f'Result: {n1} + {n2} = {n1+n2}')
                    history.append(f'{n1} + {n2} = {n1+n2}')
                elif user == 2:
                    print(f'Result: {n1} - {n2} = {n1-n2}')
                    history.append(f'{n1} - {n2} = {n1-n2}')
                elif user == 3:
                    print(f'Result: {n1} x {n2} = {n1*n2}')
                    history.append(f'{n1} x {n2} = {n1*n2}')
                elif user == 4:
                    try:
                        print(f'Result: {n1} ÷ {n2} = {round(n1/n2, 3)}')
                        history.append(f'{n1} ÷ {n2} = {round(n1/n2, 3)}')
                    except ZeroDivisionError:
                        print('❌ Can\'t divide by zero.')
                elif user == 5:
                    try:
                        print(f'Result: {n1} % {n2} = {n1%n2}')
                        history.append(f'{n1} % {n2} = {n1%n2}')
                    except ZeroDivisionError:
                        print('❌ Can\'t divide by zero.')
                elif user == 6:
                    try:
                        print(f'Result: {n1} ^ {n2} = {n1**n2}')
                        history.append(f'{n1} ^ {n2} = {n1**n2}')
                    except OverflowError:
                        print('❌ Result too Large!')
        elif user == 7:
            try:
                num = float(input('Enter the number: '))
                if num >= 0:
                    print(f'Result: {num} ^ 0.5 = {round(num**0.5, 3)}')
                    history.append(f'{num} ^ 0.5 = {round(num**0.5, 3)}')
                else:
                    print('❌ Can\'t calculate square root for negative values.')
            except ValueError:
                print('\n❌ Invalid Input!')
        elif user == 8:
            if history == []:
                print('\nNo Calculation History Yet!')
            else:
                print('==== CALCULATION HISTORY ====')
                for i in range(len(history)):
                    print(f'{i + 1}. {history[i]}')
        elif user == 9:
            print('\n👋 Thanks for using Calculator!')
            break
        else:
            print('\n❌ Invalid Input!')