#! /usr/local/bin/python3

def main():
    sentence = input()
    a = sentence.split()
    a.reverse()
    reverse = ' '.join(a)
    print(reverse)




if __name__ == '__main__':
    main()
