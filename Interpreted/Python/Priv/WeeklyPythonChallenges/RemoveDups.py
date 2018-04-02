#! /usr/local/bin/python3

import random

def main():
    list1 = generate()
    print(list1)
    list1 = set(list1)
    list1 = list(list1)
    print(list1)
def generate():
    a = []
    for x in range(30):
        a.append(random.randint(1, 10))
    return a
if __name__ == '__main__':
    main()
