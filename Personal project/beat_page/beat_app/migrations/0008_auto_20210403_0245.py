# Generated by Django 2.2.4 on 2021-04-03 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beat_app', '0007_auto_20210403_0230'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='beat',
            name='favorited_by',
        ),
        migrations.RemoveField(
            model_name='beat',
            name='likes',
        ),
        migrations.AddField(
            model_name='user',
            name='liked_beats',
            field=models.ManyToManyField(related_name='users_who_like', to='beat_app.Beat'),
        ),
    ]