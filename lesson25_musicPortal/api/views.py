from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.models import User
from .permissions import IsManager
from .serializers import (
    UserSerializer,
    UserCreateSerializer,
    UserUpdateSerializer,
    GenreSerializer,
    ArtistSerializer,
    AlbumSerializer,
    SongSerializer, RegisterSerializer
)
from app.models import Genre, Artist, Album, Song

@api_view(['GET'])
def api_healthcheck(request):
    return Response({'status': 'ok'}, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def func_for_jwt_test(request):
    return Response({'status': 'JWT_token_ok'}, status=status.HTTP_200_OK)

@swagger_auto_schema(
    method='get',
    operation_description="Получить статус менеджера",
    responses={
        200: "Доступ менеджера получен",
        401: "Нет авторизации",
        403: "Доступ запрещен",
        404: "Ресурс не найден"
    },
)
@api_view(['GET'])
@permission_classes([IsManager])
def func_for_manager_test(request):
    return Response({'status': 'Manager_permission_ok'}, status=status.HTTP_200_OK)

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer

class UserDeleteView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GenreListCreateView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class ArtistListCreateView(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class ArtistRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class AlbumListCreateView(generics.ListCreateAPIView):
    queryset = Album.objects.select_related('artist').all()
    serializer_class = AlbumSerializer

class AlbumRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.select_related('artist').all()
    serializer_class = AlbumSerializer

class SongListCreateView(generics.ListCreateAPIView):
    queryset = Song.objects.select_related('artist', 'album', 'genre').all()
    serializer_class = SongSerializer

class SongRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.select_related('artist', 'album', 'genre').all()
    serializer_class = SongSerializer
