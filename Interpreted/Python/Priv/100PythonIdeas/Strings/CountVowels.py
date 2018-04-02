
vowels = [ 'a', 'e', 'i', 'o', 'u', 'y' ]
def main():
    total = 0
    word = input()
    for x in word:
        if x in vowels:
            total = total + 1
    print(total)

main()
