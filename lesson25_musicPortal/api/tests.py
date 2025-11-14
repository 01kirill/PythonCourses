from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from app.models import Genre, Artist, Album, Song

class GenreAPITest(APITestCase):
    def test_create_genre(self):
        url = reverse('genre-list-create')
        response = self.client.post(url, {"name": "Pop"}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_genres(self):
        Genre.objects.create(name="Rock")
        url = reverse('genre-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_retrieve_genre(self):
        genre = Genre.objects.create(name="Jazz")
        url = reverse('genre-detail', args=[genre.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_genre(self):
        genre = Genre.objects.create(name="OldName")
        url = reverse('genre-detail', args=[genre.id])
        response = self.client.patch(url, {"name": "NewName"}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        genre.refresh_from_db()
        self.assertEqual(genre.name, "NewName")

    def test_delete_genre(self):
        genre = Genre.objects.create(name="DeleteMe")
        url = reverse('genre-detail', args=[genre.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class ArtistAPITest(APITestCase):
    def test_create_artist(self):
        url = reverse('artist-list-create')
        response = self.client.post(url, {"name": "Artist A"}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_artists(self):
        Artist.objects.create(name="X")
        url = reverse('artist-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_retrieve_artist(self):
        artist = Artist.objects.create(name="A1")
        url = reverse('artist-detail', args=[artist.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_artist(self):
        artist = Artist.objects.create(name="Old")
        url = reverse('artist-detail', args=[artist.id])
        response = self.client.patch(url, {"name": "New"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        artist.refresh_from_db()
        self.assertEqual(artist.name, "New")

    def test_delete_artist(self):
        artist = Artist.objects.create(name="Del")
        url = reverse('artist-detail', args=[artist.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class AlbumAPITest(APITestCase):
    def setUp(self):
        self.artist = Artist.objects.create(name="A1")

    def test_create_album(self):
        url = reverse('album-list-create')
        data = {
            "title": "ALB1",
            "artist_id": self.artist.id,
            "release_year": 1999
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_albums(self):
        Album.objects.create(title="AL 1", artist=self.artist)
        url = reverse('album-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_album(self):
        album = Album.objects.create(title="ALX", artist=self.artist)
        url = reverse('album-detail', args=[album.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_album(self):
        album = Album.objects.create(title="Old", artist=self.artist)
        url = reverse('album-detail', args=[album.id])
        response = self.client.patch(url, {"title": "New"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        album.refresh_from_db()
        self.assertEqual(album.title, "New")

    def test_delete_album(self):
        album = Album.objects.create(title="Del", artist=self.artist)
        url = reverse('album-detail', args=[album.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class SongAPITest(APITestCase):
    def setUp(self):
        self.artist = Artist.objects.create(name="AR1")
        self.album = Album.objects.create(title="AL1", artist=self.artist)
        self.genre = Genre.objects.create(name="Rock")

    def test_create_song(self):
        url = reverse('song-list-create')
        data = {
            "title": "Song1",
            "artist_id": self.artist.id,
            "album_id": self.album.id,
            "genre_id": self.genre.id,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_songs(self):
        Song.objects.create(title="S1", artist=self.artist)
        url = reverse('song-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_song(self):
        song = Song.objects.create(title="SS", artist=self.artist)
        url = reverse('song-detail', args=[song.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_song(self):
        song = Song.objects.create(title="Old", artist=self.artist)
        url = reverse('song-detail', args=[song.id])
        response = self.client.patch(url, {"title": "New"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        song.refresh_from_db()
        self.assertEqual(song.title, "New")

    def test_delete_song(self):
        song = Song.objects.create(title="Del", artist=self.artist)
        url = reverse('song-detail', args=[song.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)