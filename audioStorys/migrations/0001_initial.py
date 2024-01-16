# Generated by Django 5.0.1 on 2024-01-15 17:59

import audioStorys.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AudioStory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('text', models.TextField()),
                ('translation_text', models.TextField()),
                ('keywords', models.JSONField()),
                ('questions', models.JSONField()),
                ('audio', models.FileField(upload_to=audioStorys.models.audio_file_name)),
                ('level', models.CharField(default='A2-B1', max_length=6)),
            ],
        ),
    ]