# Generated by Django 4.1.3 on 2022-11-17 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jams', '0003_song'),
    ]

    operations = [
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='none given', max_length=30)),
                ('description', models.CharField(default='none given', max_length=150)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
