# Generated by Django 2.2.4 on 2020-12-27 02:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('beat_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Beat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favorited_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorited_by', to='beat_app.User')),
            ],
        ),
    ]
