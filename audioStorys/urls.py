from django.urls import path
from .views import *


urlpatterns = [
    path('audioStory/<int:amount>/', AudioStoryListView.as_view(), name='audioStory-list'),
    path('audioStory/create/', AudioStoryCreateView.as_view(), name='audioStory-create'),
]