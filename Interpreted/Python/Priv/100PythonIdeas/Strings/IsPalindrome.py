
def main():
    word = input()
    value = False
    i = 1
    a = len(word)
    a = a/2
    for x in word:
        if i > int(a):
            break
        y = word[i * -1]
        if x is y:
            value = True
        else: value = False
        i += 1


    if value: print('yes')
    else: print('no')
main()
