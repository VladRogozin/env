from django.db import models


def audio_file_name(instance, filename):
    new_filename = f"{instance.title}_audioStory.mp3"
    return f'audio/{new_filename}'


class AudioStory(models.Model):
    title = models.CharField(max_length=255,)
    text = models.TextField()
    translation_text = models.TextField()
    keywords = models.JSONField()
    questions = models.JSONField()
    audio = models.FileField(upload_to=audio_file_name)
    level = models.CharField(max_length=6, default='A2-B1')
