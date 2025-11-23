from django.urls import path
from .views import unico

urlpatterns = [
    path('', unico, name='unico'),
]
