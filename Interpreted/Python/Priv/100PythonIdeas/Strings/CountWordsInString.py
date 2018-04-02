
def main():
    print('Read from file: 1\nRead from console: 2')
    mode = int(input())
    if mode is 2:
        sentence = input()
        count = 1
        for letter in sentence:
            if letter is ' ':
                count += 1
        print(count)
    elif mode is 1:
        file_name = input('Enter file name: ')
        f = open(file_name + '.txt')
        phrase = f.read()
        count = 1
        for letter in phrase:
            if letter is ' ':
                count += 1
        print(count)
        print(phrase)

    else: print('Wrong input')
main()
