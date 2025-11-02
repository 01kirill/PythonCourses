from django.contrib import admin
from app.models import Artist, Album, Song, Genre

class AlbumInline(admin.TabularInline):
    model = Album
    extra = 1
    fields = ("id", "title", "artist", "release_year")

class SongInline(admin.TabularInline):
    model = Song
    extra = 1
    fields = ("id", "title", "artist", "genre")

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "date")
    search_fields = ("name",)
    list_filter = ("name", "date")
    inlines = (AlbumInline, SongInline)

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "artist", "release_year")
    search_fields = ("title", "artist__name", "release_year")
    list_filter = ("title", "artist__name", "release_year")
    inlines = (SongInline,)

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "artist", "album", "genre")
    search_fields = ("title", "artist__name", "album__title", "genre__name")
    list_filter = ("title", "artist__name", "album__title", "genre__name")

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)
    list_filter = ("name",)
    inlines = (SongInline,)
