#! /usr/local/bin/python3

import random

def main():
    a = []
    for x in range(100): a.append(random.randint(0, 300))
    a.sort()
    print(a)
    check = input()
    #for x in a:

if __name__ == '__main__':
    main()
