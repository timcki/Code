#! /usr/local/bin/python3

import requests
from bs4 import BeautifulSoup


def main():
    page = requests.get('http://www.nytimes.com/')
    soup = BeautifulSoup(page.text, 'lxml')

    for story_heading in soup.find_all(class_="story-heading"):
        if story_heading.a:
            print(story_heading.a.text.replace('\n', ' ').strip())
            print()
        else:
            print(story_heading.contents[0].strip())
            print()

if __name__ == '__main__':
    main()
