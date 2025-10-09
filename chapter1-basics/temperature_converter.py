temp = float(input('Enter temperature in Celsius: '))
print(f'''
Temperature Conversions:
{temp}°C = {(temp*9/5)+32}°F
{temp}°C = {temp+273.15}K
''')
if temp < 0:
    print('''It\'s freezing!
          ''')
temp = float(input('Enter temperature in Fahrenheit: '))
print(f'''
Temperature Conversions:
{temp}°F = {round(5*(temp-32)/9, 2)}°C''')