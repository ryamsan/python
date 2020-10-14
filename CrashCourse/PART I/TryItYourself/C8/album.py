# def make_album(artist_name, album_title):
#     album = {artist_name: album_title}
#     return album
#
# make_album('kenny g', 'songbird')


def make_album(artist, title, tracks=0):
    album_dict = {
        'artist': artist.title(),
        'title': title.title()
    }
    if tracks:
        album_dict['tracks'] = tracks
    return album_dict


album = make_album('metallica', 'ride the lightning')
print(album)

album = make_album('sia', 'the greatest')
print(album)

album = make_album('avenged sevenfold', 'nightmare')
print(album)

album = make_album('maroon 5', 'sugar', tracks=12)
print(album)
