
def make_album(artist, title, tracks=0):
    album_dict = {
        'artist': artist.title(),
        'title': title.title()
    }
    if tracks:
        album_dict['tracks'] = tracks
    return album_dict


while True:
    print("\nPlease tell me your name: ")
    print("(Enter 'q' at any time to quit.)")
    artist_input = input('Artist?: ')
    if artist_input == 'q':
        break
    title_input = input('Album\'s title?: ')
    if title_input == 'q':
        break
    album_input = make_album(artist_input, title_input)
    print(album_input)
