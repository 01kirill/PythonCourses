from rest_framework import serializers
from django.contrib.auth.models import User
from app.models import Genre, Artist, Album, Song

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError('Пароли не совпадают')
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        return User.objects.create_user(**validated_data)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
        read_only_fields = ['id']

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password'],
        )
        return user

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id', 'name', 'image', 'date']

class AlbumSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer(read_only=True)
    artist_id = serializers.PrimaryKeyRelatedField(
        queryset=Artist.objects.all(), write_only=True
    )

    class Meta:
        model = Album
        fields = ['id', 'title', 'artist', 'artist_id', 'cover', 'release_year']

    def create(self, validated_data):
        artist = validated_data.pop('artist_id')
        validated_data['artist_id'] = artist.id
        return super().create(validated_data)

class SongSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer(read_only=True)
    album = AlbumSerializer(read_only=True)
    genre = GenreSerializer(read_only=True)

    artist_id = serializers.PrimaryKeyRelatedField(
        queryset=Artist.objects.all(),
        write_only=True
    )
    album_id = serializers.PrimaryKeyRelatedField(
        queryset=Album.objects.all(),
        write_only=True,
        allow_null=True,
        required=False
    )
    genre_id = serializers.PrimaryKeyRelatedField(
        queryset=Genre.objects.all(),
        write_only=True,
        allow_null=True,
        required=False
    )

    class Meta:
        model = Song
        fields = [
            'id',
            'title',
            'artist', 'artist_id',
            'album', 'album_id',
            'genre', 'genre_id',
            'audio_file',
        ]

    def create(self, validated_data):
        artist = validated_data.pop('artist_id')
        validated_data['artist_id'] = artist.id

        album = validated_data.pop('album_id', None)
        if album:
            validated_data['album_id'] = album.id

        genre = validated_data.pop('genre_id', None)
        if genre:
            validated_data['genre_id'] = genre.id

        return super().create(validated_data)
