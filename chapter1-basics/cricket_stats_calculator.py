while True:
    try:
        runs = int(input('\nEnter runs scored: '))
        balls = int(input('Enter balls faced: '))
        fours = int(input('Enter 4s hit: '))
        sixes = int(input('Enter 6s hit: '))
    except ValueError:
        print("\nInvalid Input!")
    else:
        if ((fours*4) > runs) or ((sixes*6) > runs):
            print('\nInvalid Input!')
            print('The runs scored by fours and sixes can\'t be greater than the total runs scored.')
        else:
            print('\n===== BATTING STATS =====')
            print(f'Runs: {runs}')
            print(f'Balls: {balls}')
            try:
                strike_rate = round((runs/balls) * 100, 2)
                print(f'Strike Rate: {strike_rate}')
            except ZeroDivisionError:
                print('Strike Rate: -')
            print(f'4s: {fours} ({fours*4} runs)')
            print(f'6s: {sixes} ({sixes*6} runs)')
            try:
                boundary_percentage = round((fours*4 + sixes*6)*100/runs, 2)
                print(f'Boundary %: {boundary_percentage}')
            except ZeroDivisionError:
                print('Boundary %: -')
            print(f'Singles/Doubles: {runs - (fours*4 + sixes*6)}')
            print('=========================')
    finally:
        exit = input('\nDo you want to exit (yes/no)?: ').lower()
        if exit == 'yes':
            break