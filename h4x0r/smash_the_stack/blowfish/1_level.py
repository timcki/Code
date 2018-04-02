enc = 'GungJnfRnfl'

for x in range(0, 26):
    for letter in enc:
        if ord(letter) in range(97, 123):
            print( chr(97 + ((ord(letter) - 97 + x) % 26)), end='')
        if ord(letter) in range(65, 91):
            print( chr(65 + ((ord(letter) - 65 + x) % 26)), end='')
    print()
