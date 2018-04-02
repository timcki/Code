import os
from mutagen import mp4
# Prettier name for more readable code
def get_tags(song_path):
        return mp4.MP4('/Users/ft3/Music/lofi/{}'.format(song_path))
# Artists dict witch will be used to create albums later on or at least add song numbers cause right know this sucks balls 
Artists = {}
# List directory
for filename in os.listdir('/Users/ft3/Music/lofi'):
    #try:
    # Filename is in format *artist-songname-random_bullshit so split it into a list
    split_filename = [y.strip() for y in filename.split('-')]
    mp4_file = get_tags(filename)
    mp4_file.tags['©gen'] = 'Lofi'
    mp4_file.tags['aART'] = split_filename[0]
    mp4_file.tags['sonm'] = split_filename[1]
    mp4_file.tags['©ART'] = split_filename[0]
    mp4_file.tags['soar'] = split_filename[0]
    mp4_file.tags['©nam'] = split_filename[1]
    mp4_file.save()
    # Check if artist name already exists. If no add a new key and then append the song
    if not split_filename[0] in Artists:
        Artists[split_filename[0]] = []
    Artists[split_filename[0]].append(split_filename[1])

        #print(count, '-', split_filename)
    #except:
        #print('------------- XXXX ----------')
        #pass

for artists, songs in Artists.items():
    print(artists, '-', songs)



