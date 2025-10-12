while True:
    print('''===== CALCULATOR MENU =====
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exit
===========================
''')
    try:
        user = int(input('Choose operation (1-5): '))
    except ValueError:
        print('\nInvalid Input!')
        input('\nPress ENTER to continue...\n')
        continue
    else:
        if user in [1,2,3,4]:
            try:
                n1 = float(input('\nEnter first number: '))
                n2 = float(input('Enter second number: '))
            except ValueError:
                print('\nInvalid Input!')
            else:
                if user == 1:
                    print(f'Result: {n1} + {n2} = {n1+n2}')
                elif user == 2:
                    print(f'Result: {n1} - {n2} = {n1-n2}')
                elif user == 3:
                    print(f'Result: {n1} x {n2} = {n1*n2}')
                elif user == 4:
                    try:
                        print(f'Result: {n1} ÷ {n2} = {n1/n2}')
                    except ZeroDivisionError:
                        print('Can\'t divide by zero.')
            finally:
                input('\nPress ENTER to continue...\n')
        elif user == 5:
            print('\nThank you for using calculator!')
            break
        else:
            print('\nInvalid Input!')
            input('\nPress ENTER to continue...\n')