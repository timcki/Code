#! /usr/local/bin/python3

import requests
from bs4 import BeautifulSoup

def main():
    url = 'http://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')

    for content_section in soup.find_all(class_='content-section'):
        if content_section.p:
            f = open('scraped.txt', 'w+')
            f.write(content_section.p.contents[0])

if __name__ == '__main__':
    main()
