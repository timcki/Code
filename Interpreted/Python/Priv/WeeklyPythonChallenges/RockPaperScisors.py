#! /usr/local/bin/python3
import colorama
from colorama import Fore


def main():

    colorama.init()

    print('-------------ROCK PAPER SCISORS-------------')
    print('     Type q to quit')
    p1 = ''
    p2 = ''
    p1w = False
    draw = False
    count = 0
    while 1 > 0:
        count += 1
        print('-------------Round ' + str(count) + ' begin-------------')

        p1 = input(Fore.LIGHTRED_EX + 'Player one, Rock, Paper or Scisors?: ')
        if p1 == 'q':
            break
        p2 = input(Fore.LIGHTRED_EX + 'Player two, Rock, Paper or Scisors?: ')
        if p2 == 'q':
            break

        whoWon(p1, p2)

        if p1w:
            print(Fore.CYAN + '     Player one won, congratz!')
        elif draw:
            print(Fore.CYAN + '     It\'s a draw boys!')
        else:
            print(Fore.CYAN + '    Player two won, congratz!')

        print('-------------Round ' + str(count) + ' ended-------------')
    print('Thanks for playing!')


def whoWon(arg1, arg2):
    if arg1 == 'Rock':
        if arg2 == 'Rock':
            draw = True
        if arg2 != 'Paper':
            p1w = True
    elif arg1 == 'Paper':
        if arg1 == 'Paper':
            draw = True
        if arg2 != 'Scisors':
            p1w = True
    else:
        if arg2 == 'Scisors':
            draw = True
        if arg2 != 'Rock':
            p1w = True


if __name__ == '__main__':
    main()
