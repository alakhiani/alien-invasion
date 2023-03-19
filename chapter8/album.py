def make_album(artist, title, num_of_songs=None):
    """This function creates a dictionary describing the attributes of an album, its artist, album title, and number of songs (if supplied)"""
    album = {
        'artist' : artist,
        'title' : title,
    }
    if num_of_songs:
        album['num_of_songs'] = num_of_songs

    return album