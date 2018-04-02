#! /usr/local/bin/python3

def main():
    a = int(input())
    generateFibo(a)

def generateFibo(size):
    a = [1, 1]
    for x in range(2, size):
        a.append(a[x - 1] + a[x - 2])
    print(a)

if __name__ == '__main__':
    main()
