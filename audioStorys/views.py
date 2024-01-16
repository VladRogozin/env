from rest_framework import generics
from .models import AudioStory
from .serializers import AudioStorySerializer


class AudioStoryListView(generics.ListAPIView):
    serializer_class = AudioStorySerializer

    def get_queryset(self):
        amount = self.kwargs.get('amount', 10)

        queryset = AudioStory.objects.all()

        queryset = queryset.order_by('?')

        return queryset[:amount]


class AudioStoryCreateView(generics.CreateAPIView):
    queryset = AudioStory.objects.all()
    serializer_class = AudioStorySerializer
