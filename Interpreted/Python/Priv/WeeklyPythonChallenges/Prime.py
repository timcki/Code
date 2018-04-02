#! /usr/local/bin/python3

def main():
    number = int(input())
    result = False
    if number is 1 or number is 2:
        result = True
    else: result = IsPrime(number)
    if result: print('Prime')
    else: print ('Not prime')

def IsPrime(p):
    for x in range(2, int(p/2)):
        if p % x is 0: return False
    return True

if __name__ == '__main__':
	main()
