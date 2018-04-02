import requests
from requests.auth import HTTPDigestAuth

link = "https://mbasic.facebook.com/100002256167339/allactivity?timeend=1512115199&timestart=1512086400"

with requests.Session() as s:
	s.auth = ("facetymek@protonmail.com", "ptvf_Gy4HmmAH0I8fQ0A")
	s.headers.update({'x-test': 'true'})

	r = s.get(link)
	print(r.content)
