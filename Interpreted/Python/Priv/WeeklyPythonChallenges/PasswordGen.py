#! /usr/local/bin/python3
import random
#Random password generator

def main():
    print('----------RANDOM PASSWORD GENERATOR----------')
    print('[*] Strong password: 1')
    print('[*] Weak password:   2')
    PassType = int(input('Choose one:  '))

    if PassType is 1:
        length = int(input('What\'s the length?: '))
        password = StrongPassGen(length)

    else:
        count = int(input('How many words?:  '))
        password = WeakPasswordGen(count)

    print('Your password is:\n' + password)


def StrongPassGen(length):
    password = ''
    chars = '§1234567890-=qwertyuiop[]asdfghjkl;\'\`zxcvbnm,./£!@#$%^&*()_+QWERTYUIOP{}ASDFGHJKL:"|~ZXCVBNM<>?"\''
    for x in range(length):
        password += random.choice(chars)
    return password


def WeakPasswordGen(count):

    password = ''
    f = open('WordList.txt')
    words = f.read()
    wordList = words.split()
    for x in range(count):
        password += wordList[random.randint(0, 100)]
    return password


if __name__ == '__main__':
    main()
