# Generated by Django 2.2.4 on 2020-12-15 20:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tv_shows_app', '0006_auto_20201215_1802'),
    ]

    operations = [
        migrations.AddField(
            model_name='all_shows',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='all_shows',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
