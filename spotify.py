import spotipy
import words


################################ SPOTIPY SETUP #################################
spotify = spotipy.Spotify()

def get_random_songs():
    '''
    Search for random songs on spotify and returns list of dictionaries of the
    following form:
    {'uri', 'artist', 'name', 'image'}
    '''
    items = []
    while len(items) is 0:
        results = spotify.search(q=words.get_random_word())
        items = results['tracks']['items']
    songs = [{'uri': item['uri'], 'artist': item['artists'][0]['name'],
              'name': item['name'], 'image': item['album']['images'][0]['url']}
              for item in items]
    return songs
