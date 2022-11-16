from rest_framework import serializers
from jams.models import Genre, Artist, Album


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
            fields = ['name','description', 'artist', 'genre',]
    def create(self, validated_data):
        print('vdata:', validated_data)
        return Album.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.artist = validated_data.get('artist', instance.artist)
        instance.genre = validated_data.get('genre', instance.album)
        instance.save()
        return instance


#class SongSerializer(serializers.Serializer):
#    id = serializers.IntegerField(read_only=True)
#    name = serializers.CharField(required=True, allow_blank=False, max_length=30)
#    album = serializers.SlugRelatedField(
#                                many=True,
#                                read_only=True,
#                                slug_field='title'
#    )
#    artists = serializers.SlugRelatedField(
#                                many=True,
#                                read_only=True,
#                                slug_field='title'
#    )
#    class Meta:
#            model = Song
#            fields = ['name', 'album', 'artists',]
#    def create(self, validated_data):
#        return Song.objects.create(**validated_data)
#    def update(self, instance, validated_data):
#        instance.name = validated_data.get('name', instance.name)
#        instance.album = validated_data.get('album', instance.album)
#        instance.artists = validated_data.get('artists', instance.artists)
#        instance.save()
#       return instance




