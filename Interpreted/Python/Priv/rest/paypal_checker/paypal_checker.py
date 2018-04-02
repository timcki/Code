import requests
from bs4 import BeautifulSoup


def paypal():
    url = 'http://affiliate.cinstaller.com/affiliates/login.php#login'
    url_a = 'http://affiliate.cinstaller.com/affiliates/panel.php#Home'
    payload = {'username': 'michalzabik21@gmail.com', 'password': '1Qaz2Wsx3Edc'}
    # with requests.Session() as s:
    # page = s.post(url, data=payload)
    # print(page.content)
    r = requests.post(url_a, data=payload)
    print(r.content.decode('utf-8'))

paypal()
