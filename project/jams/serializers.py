from rest_framework import serializers
from jams.models import Song, Album, Genre, Playlist, Artists

class SongSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, allow_blank=False, max_length=30)
    album = serializers.SlugRelatedField(
                                many=True,
                                read_only=True,
                                slug_field='title'
    )
    artists = serializers.SlugRelatedField(
                                many=True,
                                read_only=True,
                                slug_field='title'
    )
    class Meta:
            model = Song
            fields = ['name', 'album', 'artists',]
    def create(self, validated_data):
        return Song.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.album = validated_data.get('album', instance.album)
        instance.artists = validated_data.get('artists', instance.artists)
        instance.save()
        return instance

class AlbumSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, allow_blank=False, max_length=30)
    artists = serializers.SlugRelatedField(
                                many=True,
                                read_only=True,
                                slug_field='title'
    )
    songs = serializers.SlugRelatedField(
                                many=True,
                                read_only=True,
                                slug_field='title'
    )
    class Meta:
            model = Album
            fields = ['name', 'artists', 'songs',]
    def create(self, validated_data):
        return Album.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.artists = validated_data.get('artists', instance.artists)
        instance.songs = validated_data.get('songs', instance.album)
        instance.save()
        return instance

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


class ArtistsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, allow_blank=False, max_length=30)
    description = serializers.CharField(required=True, allow_blank=False, max_length=100)
    class Meta:
        model = Artists
        fields = ['name', 'description',]
    def create(self, validated_data):
        return Artists().objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.name = validated_data.get('genre', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance