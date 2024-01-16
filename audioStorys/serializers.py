from rest_framework import serializers
from .models import AudioStory


class AudioStorySerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioStory
        fields = '__all__'
