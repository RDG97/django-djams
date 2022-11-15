from rest_framework import serializers
from jams.models import Song, LANGUAGE_CHOICES, STYLE_CHOICES

class SongSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, allow_blank=False, max_length=30)
    