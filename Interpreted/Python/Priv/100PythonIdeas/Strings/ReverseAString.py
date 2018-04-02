
def main():
    phrase = input()
    reverse = ''
    i = len(phrase)
    for x in phrase:
        reverse = reverse + (phrase[i - 1])
        i = i - 1
    print(reverse)
main()
