name = input('Enter your name: ')
age = int(input('Enter your age: '))
school = input('Enter your school: ')
subject = input('Enter your favorite subject: ')
print('===== MY INFO =====')
print(f'''Name: {name}
Age: {age}
School: {school}
Favorite Subject: {subject}
Birth Year: {2025-age}
Days Old: {age*365}
Hours Old: {age*365*24}
Minutes Old: {age*365*24*60}''')