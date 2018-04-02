#! /usr/local/bin/python3

def main():
    number = int(input())
    result = 1
    for x in range(2,number+1):
        result *= x
    print(result)



if __name__ == '__main__':
    main()
