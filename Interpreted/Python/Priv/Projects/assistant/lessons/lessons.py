#! /usr/local/bin/python3

from bs4 import BeautifulSoup
from urllib import request
import datetime


class Lessons():

    def __init__(self, class_num):
        self.which_class = class_num
        self.url = "https://www.v-lo.krakow.pl/dla-uczniow/plan-lekcji?view=class&num={}".format(self.which_class)

    def open_url(self):
        response = request.urlopen(self.url)
        page = response.read()
        soup = BeautifulSoup(page, 'html.parser')
        return soup

    def find_lessons(self):
        soup = self.open_url()
        print(self.url)
        for tr in soup.find_all('tr', class_='schedule_row0'):
            for td in tr.find_all('td'):
                print(td)
                for a in 


lessons = Lessons(14)
lessons.find_lessons()
