import hashlib
import requests

m = hashlib.md5(b'true').hexdigest()

url = 'https://felicity.iiit.ac.in/contest/extra/birthday/'

r = requests.get(url, cookies={ "birthday_invite": m })
print(r.text)
