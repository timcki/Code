#! /usr/local/bin/python3


def main():
    number = input()
    letters = input()
    count = 0

    x = []

    for letter in letters:
        if letter == 'B':
            count += 1

        else:
            if count != 0:
                x.append(count)
            count = 0

    if count != 0:
        x.append(count)

    print(len(x))
    for y in x:
        print(y, end=' ')

main()
