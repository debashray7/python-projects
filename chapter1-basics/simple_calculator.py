n1 = float(input("Enter first number: "))
n2 = float(input("Enter second number: "))
print(f'''
=====RESULTS=====
Addition: {n1+n2}
Subtraction: {n1-n2}
Multiplication: {n1*n2}
Division: {n1/n2}
Floor Division: {n1//n2}
Remainder: {n1%n2}
Power: {n1**n2}
Average: {(n1+n2)/2}
Percentage: {n1} is {round(n1*100/(n1+n2), 2)} % of {n1+n2}
==================''')