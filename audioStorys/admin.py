from django.contrib import admin
from django import forms
from .models import AudioStory
from django.db import models


@admin.register(AudioStory)
class AudioStoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'translation_text', 'keywords', 'questions', 'audio', 'level')
    search_fields = ('title', 'text', 'translation_text')
    formfield_overrides = {
        models.FileField: {'widget': forms.FileInput(attrs={'accept': 'audio/*'})},
    }