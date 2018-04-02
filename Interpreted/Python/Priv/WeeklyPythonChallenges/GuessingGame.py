#! /usr/local/bin/python3

import random

def main():
    print('----------GUESSING GAME----------')
    print('         Type q to exit')
    UserRange = int(input('What should the range be? (from 1): '))
    NumToGuess = random.randint(1, UserRange)
    tries = 0

    while 1 > 0:
        tries += 1
        GuessedNum = input('Guess the number: ')
        if GuessedNum is 'q':
            if tries > 0:
                print('\nYou gave up after ' + str(tries) + ' tries\n')
            break
        if int(GuessedNum) is NumToGuess:
            print('Congratz you guessed right!')
            print('Done in ' + str(tries) + ' tries')
            print('-----Generating another random number-----')
            print('                Type q to exit\n')
            NumToGuess = random.randint(1, UserRange)
        elif int(GuessedNum) < NumToGuess: print('Too small')
        else: print('Too big')


if __name__ == '__main__':
	main()
