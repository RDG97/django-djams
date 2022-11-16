from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=30, default='none given')
    description = models.CharField(max_length=150, default='none given')
    class Meta:
        ordering = ['id']

class Genre(models.Model):
    genre = models.CharField(max_length=20, default='none given')
    description = models.CharField(max_length=150, default='none given')
    class Meta:
        ordering = ['id']

class Album(models.Model):
    name = models.CharField(max_length=30, default='none given')
    description = models.CharField(max_length=150, default='none given')
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    class Meta:
        ordering = ['id']
#
#class Song(models.Model):
#    id = models.AutoField(primary_key=True)
#    name = models.CharField(max_length=30, default='none given')
#    artist = models.ManyToManyField(Artists)
#    album = models.ManyToManyField(Album)
#    class Meta:
#        ordering = ['id']
#
#class Playlist(models.Model):
#    id = models.AutoField(primary_key=True)
#    name = models.CharField(max_length=30, default='none given')
#    description = models.CharField(max_length=150, default='none given')
#    class Meta:
#        ordering = ['id']
#
#