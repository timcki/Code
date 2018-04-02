#! /usr/local/bin/python3

import random

def main():
    print('===========COWS AND BULLS===========')
    print('          Type q to exit')

    Number = randomNumberGen()
    print('Enter a number:')
    while 1 > 0:
        GuessedNum = input('>>> ')
        print(Number)
        if GuessedNum == 'q':
            print('Thanks for playing')
            break
        elif GuessedNum == Number:
            print('Congratz you won!')
            print('==========Generating new number==========\n')
            Number = randomNumberGen()
        else:
            check(GuessedNum, Number)
            print(Number)
            print(check)



def randomNumberGen():
    RanNum = str(random.randint(1000, 9999))
    return RanNum


def check(UserInput, NumToCheck):
    cowbulls = [0, 0]
    for i in range(len(NumToCheck)):
        if NumToCheck[i] == UserInput[i]: cowbulls[1] += 1
        else: cowbulls[0] += 1
    return cowbulls




if __name__ == '__main__':
    main()
