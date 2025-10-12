while True:
    print('''===== TEMPERATURE CONVERSION =====
1. Celsius to Fahrenheit and Kelvin
2. Fahrenheit to Celsius and Kelvin
3. Kelvin to Celsius and Fahrenheit
4. Exit
==================================''')
    try:
        user = int(input('Choose operation (1-4): '))
    except ValueError:
        print('\nInvalid Input!\n')
    else:
        if user in [1,2,3]:
            try:
                temp = float(input('\nEnter temperature: '))
            except ValueError:
                print('\nInvalid Input!')
            else:
                if user == 1:
                    if temp < -273.15:
                        print('\nInvalid Input! Temperature can\'t be below -273.15°C.')
                    else:
                        print('\nTemperature Conversions:')
                        print(f'{temp}°C = {(temp*9/5)+32}°F')
                        print(f'{temp}°C = {temp + 273.15}K')
                        if temp <= 0:
                            print('\nIt\'s freezing! 🥶')
                elif user == 2:
                    if temp < -459.67:
                        print('\nInvalid Input! Temperature can\'t be below -459.67°F.')
                    else:
                        print('\nTemperature Conversions:')
                        print(f'{temp}°F = {round((temp-32)*5/9, 2)}°C')
                        print(f'{temp}°F = {round((temp-32)*5/9, 2) + 273.15}K')
                        if temp <= 32:
                            print('\nIt\'s freezing! 🥶')
                elif user == 3:
                    if temp < 0:
                        print('\nInvalid Input! Temperature can\'t be below 0K.')
                    else:
                        print('\nTemperature Conversions:')
                        print(f'{temp}K = {round(temp - 273.15, 2)}°C')
                        print(f'{temp}K = {round((temp-305.15)*5/9, 2)}°F')
                        if temp <= 273.15:
                            print('\nIt\'s freezing! 🥶')
            finally:
                print('\n==================================\n')
        elif user == 4:
            print('\nThanks for using Temperature Converter!')
            break
        else:
            print('\nInvalid Input!\n')