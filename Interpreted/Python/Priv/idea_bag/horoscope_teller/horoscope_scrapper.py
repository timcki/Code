class HoroscopeGrabber():

    def __init__(self, horoscope):
        self.url = 'https://www.astrology.com/horoscope/daily/{}.html'.format(horoscope)

    def get_url(self):
        import requests
        r = requests.get(self.url)
        return r

    def parse_horoscope(self):
        from bs4 import BeautifulSoup as bs
        page = self.get_url()
        contents = page.content
        soup = bs(contents, 'html.parser')
        horoscope = soup.find('div', class_='page-horoscope-text')
        return horoscope.text

    def print_horoscope(self):
        horoscope = self.parse_horoscope()
        h_better = horoscope.split('.')
        for phrase in h_better[:-1]:
            print(phrase.strip() + '.')
