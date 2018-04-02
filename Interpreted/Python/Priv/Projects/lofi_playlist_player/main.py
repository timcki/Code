from lxml import html
from urllib import request

# Download url
url = request.urlopen('https://www.youtube.com/playlist?list=PLs7d4DToZ-ovEUtKLAaLI2Cz_UpNUt35A')

# Parse into lxml tree
tree = html.fromstring(url.read())

# Iter through all the links in page and select those with /watch in then. Delete duplicates
# TODO Make this efficient and not a helf ass solution boiii
links = []
for x in tree.iterlinks():
    if '/watch' in x[2] and x[2].split('&')[0] not in links:
        links.append(x[2].split('&')[0])

print(links)

with open('/Users/ft3/Music/lofi_playlist', 'a') as lofi_playlist_file:
    for x in links:
        tmp = 'https://www.youtube.com' + x + '\n'
        print(tmp)
        lofi_playlist_file.write(tmp)
