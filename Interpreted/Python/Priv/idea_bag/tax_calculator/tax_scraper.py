import requests
from bs4 import BeautifulSoup

countries = {}


def tax_scraper():
    page = requests.get('https://www.ricksteves.com/travel-tips/money/vat-rates-in-europe')
    contents = page.content
    soup = BeautifulSoup(contents, 'html.parser')
    for row in soup.find_all('tr'):
        for cell, number in zip(row.find_all('td'), range(0, 2)):
            if number == 0:
                name = cell.text.strip()
            else:
                countries[name] = int(cell.text.strip()[:-1])

    return countries


# for cell in soup.find_all('td', class_='sortkey'):
    # print(p.findall(cell.text))
