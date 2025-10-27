from django.contrib import admin
from .models import Game, Order

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'price')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'total', 'created')
    list_filter = ('created',)
