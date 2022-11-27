from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('article/<int:news_id>', article, name='article')
]


