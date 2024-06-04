class Song:
    pass
    
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.genre = genre
        self. artist = artist
        Song.increase_count()
        Song.add_genres(genre)
        Song.add_artists(artist)
        Song.add_genre_count(genre)
        Song.add_artist_count(artist)

    @classmethod
    def increase_count(cls, increment = 1):
        cls.count += increment

    @classmethod
    def add_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_genre_count(cls, genre):
        if cls.genre_count.get(genre):
            cls.genre_count[genre]+= 1
        else:
            cls.genre_count[genre]= 1

    @classmethod
    def add_artist_count(cls, artist):
        if cls.artist_count.get(artist):
            cls.artist_count[artist]+= 1
        else:
            cls.artist_count[artist]= 1