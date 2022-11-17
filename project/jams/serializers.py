from rest_framework import serializers
from jams.models import Genre, Artist, Album, Song, Playlist, Playlist_songs

class GenreSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    genre = serializers.CharField(required=True, allow_blank=False, max_length=30)
    description = serializers.CharField(required=True, allow_blank=False, max_length=100)
    class Meta:
        model = Genre
        fields = ['genre', 'description',]
    def create(self, validated_data):
        return Genre.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.genre = validated_data.get('genre', instance.genre)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance

class ArtistSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, allow_blank=False, max_length=30)
    description = serializers.CharField(required=True, allow_blank=False, max_length=100)
    class Meta:
        model = Artist
        fields = ['name', 'description',]
    def create(self, validated_data):
        return Artist.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance

class AlbumSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, allow_blank=False, max_length=30)
    description = serializers.CharField(required=True, allow_blank=False, max_length=100)
    artist = serializers.PrimaryKeyRelatedField(
    many=False,
    queryset=Artist.objects.all()
    )
    genre = serializers.PrimaryKeyRelatedField(
    many=False,
    queryset=Genre.objects.all()
    )
    class Meta:
            model = Album
            fields = ['id', 'name','description', 'artist', 'genre',]
    def create(self, validated_data):
        print('vdata:', validated_data)
        return Album.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.artist = validated_data.get('artist', instance.artist)
        instance.genre = validated_data.get('genre', instance.genre)
        instance.save()
        return instance

class SongSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, allow_blank=False, max_length=30)
    duration = serializers.FloatField(required=True)
    artist = serializers.PrimaryKeyRelatedField(
    many=False,
    queryset=Artist.objects.all()
    )
    album = serializers.PrimaryKeyRelatedField(
    many=False,
    queryset=Album.objects.all()
    )
    class Meta:
            model = Song
            fields = ['id', 'name','duration', 'artist', 'album',]
    def create(self, validated_data):
        return Song.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.duration = validated_data.get('duration', instance.duration)
        instance.artist = validated_data.get('artist', instance.artist)
        instance.album = validated_data.get('album', instance.album)
        instance.save()
        return instance

class PlaylistSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, allow_blank=False, max_length=30)
    description = serializers.CharField(required=True, allow_blank=False, max_length=100)
    class Meta:
            model = Song
            fields = ['id', 'name','description',]
    def create(self, validated_data):
        return Playlist.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance

class PlaylistSongsSerializer(serializers.ModelSerializer):
    playlist = serializers.PrimaryKeyRelatedField(
    many=False,
    queryset=Playlist.objects.all()
    )
    song = serializers.PrimaryKeyRelatedField(
    many=False,
    queryset=Song.objects.all()
    )
    class Meta:
            model = Playlist_songs
            fields = ['playlist', 'song',]
    def create(self, validated_data):
        return Playlist_songs.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.playlist = validated_data.get('playlist', instance.playlist)
        instance.song = validated_data.get('song', instance.song)
        instance.save()
        return instance