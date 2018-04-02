#! /usr/local/bin/python3
def main():
    n = int(input())
    n = n / 2
    for x in range(2, int(n + 1)):
        if n % x == 0:
            print(x)

main()
