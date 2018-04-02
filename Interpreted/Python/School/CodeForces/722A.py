#! /usr/local/bin/python3

def main():
    tformat = input()
    hour = input()

    x = hour.split(':')

    hourValue = x[0]
    minuteValue = x[1]
    if tformat == 12:
        if hourValue <= 12 and hourValue != 0:
            if hourValue[0] > 1:
                hourValue[0] = 1
            elif minuteValue >= 59:
                minuteValue[0] = 3
    final = ':'.join((hourValue, minuteValue))
    print(final)


main()
