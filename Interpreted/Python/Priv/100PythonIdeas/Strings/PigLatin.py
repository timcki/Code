
def main():
    word = input()
    i = len(word)
    proper = word[1:i] + word[0] + 'ay'
    print(proper)
main()
