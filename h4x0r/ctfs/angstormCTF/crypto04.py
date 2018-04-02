import termcolor
ct = 'vfauedwyedmtlwylwnawyjfdzltqilqdezfntmwyewyejzettjedmwyfjlzettjyeilwfplxaenmlmpvbldzqwyxadjzyfjxfddemfqwvfavfatwzlqdplnxqyeilexnlewlnnljsfdjqpqtqwvwyedvfauedsfjjqptvoewyfbvfazllsofnjedwqexfedmvfauanjlwylbenqdljvfayeilwyewtaranvvfayeilwyltaranvfodfwcdfzqdxzyewqcdfzwyewjedwqexfjmlewyzyqtlwnexqusnfpeptvjeilmtqiljedmbvlrqjwldulzyqtlxnfwljgaledmqdufbsnlyldjqptlwfvfajeiljtqiljvfamfdwzedwwylwnawyplueajlmllsmfzdqdsteuljvfamfdwwetcepfawewsenwqljvfazedwblfdwyewzettvfadllmblfdwyewzettzlajlzfnmjtqclyfdfnufmltfvetwvzlajlwyljlzfnmjejwylpeucpfdlwfetqoljsldwmloldmqdxjfblwyqdxvfaajllbejesaduytqdlqyeildlqwylnwylwqbldfnwylqdutqdewqfdwflrsteqdbvjltowfebedzyfnqjljedmjtllsjadmlnwylptedclwfowylilnvonllmfbqsnfiqmlwyldgaljwqfdjwylbeddlnqdzyquyqsnfiqmlqwqmnewylnvfahajwjeqmwyedcvfaedmzldwfdvfanzevfwylnzqjlqjaxxljwvfasqucasezlesfdedmjwedmesfjwlqwylnzevqmfdwxqilemebdzyewvfawyqdcvfanlldwqwtlmwf{olzxffmbldhljjls}'

d = {}
dt = ''
for x in ct:
    try:
        d[x] += 1
    except:
        d[x] = 1

for w in sorted(d, key=d.get, reverse=True):
    print(w, termcolor.colored(d[w], 'cyan'))

def lol(x):
    a = {
            'v': 'y',
            'f': 'o',
            'a': 'u',
            'u': 'c',
            'e': 'a',
            'd': 'n',
            'w': 't',
            'x': 'g',
            'm': 'd',
            'z': 'w',
            'y': 'o',
            'c': 'k',
            'q': 'i',
            'j': 's',
            'o': 'f',
            'l': 'e',
            'b': 'm',
        }
    try:
        return termcolor.colored(a[x], 'yellow')
    except:
        return termcolor.colored(x, 'blue')

dt = ''.join([lol(x) for x in ct])

termcolor.cprint('='*10 + ' CT ' + '=' * 10, 'green')
print(ct)
termcolor.cprint('*'*10 + ' DT ' + '*'*10, 'green')
print(dt)
