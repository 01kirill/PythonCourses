import debug_toolbar
from django.contrib.auth.views import LogoutView
from django.urls import path, include

from app.views import register_view, main_view, artist_view, login_view

urlpatterns = [
    path('', main_view, name='main'),
    path('artist/<int:artist_id>/', artist_view, name='artist'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('__debug__/', include(debug_toolbar.urls)),
]
