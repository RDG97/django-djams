# Generated by Django 4.1.3 on 2022-11-17 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jams', '0002_rename_artist_album_artist_rename_genre_album_genre'),
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='none given', max_length=30)),
                ('duration', models.FloatField(default=4.2)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jams.album')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jams.artist')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
