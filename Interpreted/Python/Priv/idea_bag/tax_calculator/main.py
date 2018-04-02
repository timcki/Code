from tax_scraper import tax_scraper as tax_s


def calculate_price_localy(price, percent):
    percent = percent / 100
    return price + (price * percent)


def calculate_price_remotly(price, country):
    dic = tax_s()
    percent_l = dic[country]
    percent_l = percent_l / 100
    return price + (price * percent_l)


def main():
    print('=== TAX CALCULATOR ===')
    print('Only works for countries in EU!')
    price = float(input('Enter the price (eg. 45.67): '))
    print(price)
    p_c = input('Enter tax amount or your country (eg. 23% or Poland): ')
    try:
        p_c = float(p_c[:-1])
        total_value = calculate_price_localy(price, p_c)
    except:
        total_value = calculate_price_remotly(price, p_c)

    print('Price before tax: ' + str(price))
    print('Price after tax: {0:.2f}'.format(total_value))


main()
