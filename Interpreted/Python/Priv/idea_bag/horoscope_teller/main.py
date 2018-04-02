import horoscope_scrapper as h_s

horoscope_dict = { 1:['Aries', '03/21 - 04/19'], 2:['Taurus', '04/20 - 05/20'], 3:['Gemini', '05/21 - 06/20'], 4:['Cancer', '06/21 - 07/22'],
5:['Leo', '07/23 - 08/22'], 6:['Virgo', '08/23 - 09/22'], 7:['Libra', '09/23 - 10/22'], 8:['Scorpio', '10/23 - 11/21'],
9:['Sagittarius', '11/22 - 12/21'], 10:['Capricorn', '12/22 - 01/19'], 11:['Aquarius', '01/20 - 02/18'], 12:['Pisces', '02/19 - 03/20']}


def main():
    print('===== HOROSCOPE TELLER =====')
    print('Input the number corresponding to your horoscope:')
    for x in horoscope_dict:
        if x == 9 or x == 10 or x == 11:
            print(str(x) + ')\t' + horoscope_dict[x][0] + '\t' +horoscope_dict[x][1])
            continue
        print(str(x) + ')\t' + horoscope_dict[x][0] + '\t\t' +horoscope_dict[x][1])

    x = int(input('==> '))
    for y in horoscope_dict[x]:
        print(y, end='\t\n')

    horoscope = h_s.HoroscopeGrabber(horoscope_dict[x][0].lower())
    horoscope.print_horoscope()


if __name__ == '__main__':
    main()
