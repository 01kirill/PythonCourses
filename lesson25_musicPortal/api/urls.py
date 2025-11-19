from django.urls import path
from .views import (
    api_healthcheck,
    func_for_jwt_test
)
from .views import (
    UserListView,
    UserCreateView,
    UserDetailView,
    UserUpdateView,
    UserDeleteView,
    GenreListCreateView,
    GenreRetrieveUpdateDestroyView,
    ArtistListCreateView,
    ArtistRetrieveUpdateDestroyView,
    AlbumListCreateView,
    AlbumRetrieveUpdateDestroyView,
    SongListCreateView,
    SongRetrieveUpdateDestroyView
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('healthcheck/', api_healthcheck),
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/create/', UserCreateView.as_view(), name='user-create'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('users/<int:pk>/update/', UserUpdateView.as_view(), name='user-update'),
    path('users/<int:pk>/delete/', UserDeleteView.as_view(), name='user-delete'),
    path('genres/', GenreListCreateView.as_view(), name='genre-list-create'),
    path('genres/<int:pk>/', GenreRetrieveUpdateDestroyView.as_view(), name='genre-detail'),
    path('artists/', ArtistListCreateView.as_view(), name='artist-list-create'),
    path('artists/<int:pk>/', ArtistRetrieveUpdateDestroyView.as_view(), name='artist-detail'),
    path('albums/', AlbumListCreateView.as_view(), name='album-list-create'),
    path('albums/<int:pk>/', AlbumRetrieveUpdateDestroyView.as_view(), name='album-detail'),
    path('songs/', SongListCreateView.as_view(), name='song-list-create'),
    path('songs/<int:pk>/', SongRetrieveUpdateDestroyView.as_view(), name='song-detail'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('check_jwt/', func_for_jwt_test),
]
