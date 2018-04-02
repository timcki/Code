#! /usr/local/bin/python3


def main():
    people = input()
    people = people.replace(' ', '')
    g = int(people[0])
    c = int(people[1])

    if g != 0 or c == 0:
        if c > g:
            print(c, end=' ')
        else:
            print(g, end=' ')
        if c != 0:
            print(c + g - 1)
        else:
            print(g)
    else:
        print('Impossible')

main()
