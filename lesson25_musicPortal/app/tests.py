from django.test import TestCase
from .models import Genre, Artist, Album, Song
from datetime import date

class GenreModelTest(TestCase):
    def test_genre_str(self):
        genre = Genre.objects.create(name="Rock")
        self.assertEqual(str(genre), "Rock")

class ArtistModelTest(TestCase):
    def test_artist_str(self):
        artist = Artist.objects.create(name="Artist 1")
        self.assertEqual(str(artist), "Artist 1")

    def test_artist_with_date(self):
        artist = Artist.objects.create(name="A2", date=date(2020, 1, 1))
        self.assertEqual(artist.date.year, 2020)

class AlbumModelTest(TestCase):
    def setUp(self):
        self.artist = Artist.objects.create(name="Artist")

    def test_album_str(self):
        album = Album.objects.create(title="Album 1", artist=self.artist, release_year=2000)
        self.assertEqual(str(album), "Album 1 — Artist")

class SongModelTest(TestCase):
    def setUp(self):
        self.artist = Artist.objects.create(name="A1")
        self.album = Album.objects.create(title="AL1", artist=self.artist)
        self.genre = Genre.objects.create(name="Rock")

    def test_song_str(self):
        song = Song.objects.create(title="S1", artist=self.artist)
        self.assertEqual(str(song), "S1 — A1")

    def test_song_with_album_and_genre(self):
        song = Song.objects.create(title="S2", artist=self.artist, album=self.album, genre=self.genre)
        self.assertEqual(song.album.title, "AL1")
        self.assertEqual(song.genre.name, "Rock")
