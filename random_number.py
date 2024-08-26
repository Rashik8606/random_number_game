import random
import logo_art

EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5
def set_defficality(level_choose):
    if level_choose == 'easy':
        return EASY_LEVEL_ATTEMPTS
    elif level_choose == 'hard':
        return HARD_LEVEL_ATTEMPTS
    else:
        return

def check_number(guessed_number,answer,attempts):
    if guessed_number < answer:
        print('you guess too low ')
        return attempts-1
    elif guessed_number >answer:
        return attempts-1
    else:
        print(f'your guess is right ..the answer was {answer}')

def game():
    print(logo_art.logo)
    print('Welcome th the number :gussing game')
    print('im Thinking of a Number Between 1 to 100')
    answer = random.randint(1,50)
    level = input('choose level of difficulty easy or hard :')
    guessed_number = 0
    attempts = set_defficality(level)
    while guessed_number != answer:
        print(f'you have {attempts} rmaining attempts')
        guessed_number = int(input('guess a number :'))
        attempts= check_number(guessed_number,answer,attempts)
        if attempts == 0:
            print('you have out of guesses..you lose !')
            return 
        elif guessed_number!=answer:
            print('guess again')
game()