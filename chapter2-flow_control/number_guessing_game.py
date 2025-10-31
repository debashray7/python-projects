import random

print('===== ADVANCED GUESSING GAME =====')

def difficulty():
    level = input('\nEnter difficulty level (easy, medium, hard): ').lower()
    if level == 'easy':
        return 15
    elif level == 'medium':
        return 10
    elif level == 'hard':
        return 7
    else:
        print('\nInvalid Input! Setting difficulty level to medium...')
        return 10

def proximity(user, computer):
    diff = abs(user - computer)
    if diff <= 10:
        print('Very close!')
    elif diff <= 50:
        print('Close!')
    elif diff < 200:
        print('Far!')
    else:
        print('Very far!')

def main_game():
    score = []  
    
    while True: 
        num = random.randint(1, 1000)
        attempts = 1
        difficulty_level = difficulty()
        print('\nI\'m thinking of a number between 1-1000')
        print('You have 10 attempts. Good luck!') 
        
        while attempts <= difficulty_level:   
            print(f'\nAttempt {attempts}/{difficulty_level}')
            try:
                user_num = int(input('Your guess: '))
                
                if user_num > num:
                    print('Too High!', end=' ')
                    proximity(user_num, num)
                elif user_num < num:
                    print('Too Low!', end=' ')
                    proximity(user_num, num)
                else:
                    print(f'🎉 CORRECT! You guessed it in {attempts} attempts!')
                    score.append(attempts)
                    print(f'\nBest Score: {min(score)}')
                    break
                
                attempts += 1
            except ValueError:
                print('\nInvalid Input!')
                break

        else:
            print('\nYou ran out of attempts!')
            print(f'The number was {num}.')
        
        response = input('\nPlay again? (yes/no): ').lower()
        print('==================================')
        
        if response != 'yes':
            print('👋 Thank you for playing Number Guessing Game!')
            break

main_game()