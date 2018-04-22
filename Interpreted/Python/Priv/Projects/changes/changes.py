from bs4 import BeautifulSoup
from urllib import request

class Changes():


    # Initialize the object with changes for the current day or the next one depending on time of the day ( am or pm )
    def __init__(self):

        import datetime

        self.tmp = []
        self.changes = []
        self.changes_dict = dict()
        if datetime.datetime.now().hour < 12:
            self.url = 'https://www.v-lo.krakow.pl/dla-uczniow/zastepstwa'
        else:
            self.url = 'https://www.v-lo.krakow.pl/dla-uczniow/zastepstwa?t=1'

    # Download url and pass the bs4 object
    def open_url(self):
        try:
            response = request.urlopen(self.url)
        except:
            raise Exception(colored('Dupa nie internet', 'red'))
        page = response.read()
        return BeautifulSoup(page, 'html.parser')

    # What the actual duck
    def extract_changes(self, soup):
        for table in soup.find_all('table'):
            for change in table('td', class_='record_3'):
                self.tmp.append(change.text)
            self.changes.append(self.tmp)
            self.tmp = []

        for teacher, x in zip(soup.find_all('h3', class_='table_title'), self.changes):
            self.changes_dict[teacher.text] = x
        return self.changes_dict

    # Function run by the "user" to print changes in a pretty way and fetch them beforehand
    def fetch_changes(self):
        url = self.open_url()
        self.fetched_changes = self.extract_changes(url)
        self.print_changes()

    # Afraid to touch without breaking the whole thing
    def print_changes(self):
        from termcolor import colored

        print()
        print(colored(datetime.date.today(), 'red'))
        print()
        for x in self.fetched_changes:
            if 'Szewczyk' in x or x == 'Agnieszka Olszewska - Rabiega':
                print(colored(x, 'green'), end='\n\n')
                print('\t' + colored('Zmiany na jezykach', 'red'), end='\n\n')
                continue
            print(colored(x, 'green') + '\n')
            for y in self.fetched_changes[x]:
                if str(y[0:2]) == '3D':
                    print('\t' + colored(y, 'red'))
                elif str(y[0:2]) == '2G':
                    print('\t' + colored(y, 'cyan'))
                elif str(y[0:2]) == '3H':
                    print('\t' + colored(y, 'yellow'))
                else:
                    print('\t' + colored(y, 'blue'))
            print('\n---------------------\n')

    def irc_changes(self):
        url = self.open_url()
        self.fetched_changes = self.extract_changes(url)
        print(self.fetched_changes)
