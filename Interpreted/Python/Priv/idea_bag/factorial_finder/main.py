global recursion_final

def main():
    factorial = int(input('Input the number to factorialize: '))
    if factorial == 0:
        print('1')
    way = int(input('Compute it:\n1) Using recursion\n2) Using a loop\n: '))

    if way != 1 and way != 2:
        print('Debil')

    if way == 1:
        recursion(factorial)
    else:
        print(loop(factorial))


def loop(factorial):
    final = 1
    for x in range(factorial, 0, -1):
        final *= x
    return final


def recursion(factorial):
    global recursion_final
    return 0

main()
