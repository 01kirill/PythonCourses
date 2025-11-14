from django.urls import path
from .views import api_healthcheck

urlpatterns = [
    path('healthcheck/', api_healthcheck)
]
