from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.game_list, name='game_list'),
    path('game/<slug:slug>/', views.game_detail, name='game_detail'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/add/<int:game_id>/', views.cart_add, name='cart_add'),
    path('cart/remove/<int:game_id>/', views.cart_remove, name='cart_remove'),
    path('order/', views.make_order, name='make_order'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
