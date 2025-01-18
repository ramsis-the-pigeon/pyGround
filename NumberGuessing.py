from random import randint
random = randint(1, 100)
attempts = 10

is_running = True

while is_running :
    
    guess = int(input('guess a number between 1 and 100: ')) 
    
    if guess < random:
        print("too low")
        attempts = attempts - 1
    elif guess > random:
        print("too high")
        attempts = attempts - 1
    elif guess == random:
        print('thats correct \n You win')
        print(f'Your score is {attempts * 10}/100')
        options = input('Press A to play again, Q to quite: ').upper()
        if options == 'A':
            attempts = 10
            random = randint(1, 100)
            continue
        elif options == 'Q':
            is_running = False
    if not attempts:
        print('You ran out of Attempts')
        options = input('Press A to play again, Q to quite: ').upper()
        if options == 'A':
            pass
        elif options == 'Q':
            is_running = False
    
    
    
