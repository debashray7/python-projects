print('===== PALINDROME CHECKER =====')
num = 0
while True:
    text = input('\nEnter a word/number: ')
    text_used = text.lower().replace(' ','')
    if text_used == text_used[::-1]:
        print(f'✅ "{text}" is a palindrome!\n')
        num += 1
    else:
        print(f'❌ "{text}" is NOT a palindrome.\n')
    check_another = input('Check another? (yes/no): ').upper()
    if check_another in ['YES', 'NO']:
        if check_another == 'NO':
            print(f'\nTotal palindromes found: {num}')
            print('==============================')
            print('Thank you for using Palindrome Checker! 👋')
            break
    else:
        print('\n❌ Invalid Input!')
        permission = input('Do you want to continue? (yes/no): ').upper()
        if permission != 'YES':
            break