# Generated by Django 3.2 on 2021-05-03 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0005_video_allowed_memberships'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='allowed_memberships',
        ),
        migrations.RemoveField(
            model_name='video',
            name='membership',
        ),
    ]
