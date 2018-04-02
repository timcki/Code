#! /usr/local/bin/python3

def main():
    number = input()
    a = 0
    for x in number:
        a += int(x)
    if int(number) % a == 0:
        print('is hashad')
    else: print('is not hashad')

if __name__ == '__main__':
    main()
