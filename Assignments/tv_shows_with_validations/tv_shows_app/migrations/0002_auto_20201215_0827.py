# Generated by Django 2.2.4 on 2020-12-15 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tv_shows_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='all_shows',
            name='release_date',
            field=models.CharField(max_length=45),
        ),
    ]
