import requests
from bs4 import BeatifulSoup

url = "https://www.v-lo.krakow.pl/dla-uczniow/zastepstwa?subsDate=2017-02-21"
r = requests.get(url)
soup = BeatifulSoup(r.content)
