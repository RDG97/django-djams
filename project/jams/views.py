from django.shortcuts import render
from rest_framework import status, generics
from django.http import HttpResponse, JsonResponse, Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from jams.models import Genre, Artist, Album, Song, Playlist, Playlist_songs
from jams.serializers import GenreSerializer, ArtistSerializer, AlbumSerializer, SongSerializer, PlaylistSerializer, PlaylistSongsSerializer
from django.http import Http404

class GenreList(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class GenreDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class ArtistList(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class ArtistDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class AlbumList(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class AlbumDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class SongList(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class SongDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class PlaylistList(generics.ListCreateAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer

class PlaylistDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer

class PlaylistSongList(generics.ListCreateAPIView):
    queryset = Playlist_songs.objects.all()
    serializer_class = PlaylistSongsSerializer

class PlaylistSongDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Playlist_songs.objects.all()
    serializer_class = PlaylistSongsSerializer


#class SongList(APIView):
#    def get(self, request, format=None):
#        songs = Song.objects.all()
#        serializer = SongSerializer(songs, many=True)
#        return Response(serializer.data)
#    def post(self, request, format=None):
#        serializer = SongSerializer(data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data, status=status.HTTP_201_CREATED)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#class SongDetail(APIView):
#    def get_object(self, pk):
#        try:
#            return Song.objects.get(pk=pk)
#        except Song.DoesNotExist:
#            raise Http404
#
#    def get(self, request, pk, format=None):
#        song = self.get_object(pk)
#        serializer = SongSerializer(song)
#        return Response(serializer.data)
#
#    def put(self, request, pk, format=None):
#        song = self.get_object(pk)
#        serializer = SongSerializer(song, data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#    def delete(self, request, pk, format=None):
#        song = self.get_object(pk)
#        song.delete()
#        return Response(status=status.HTTP_204_NO_CONTENT)



#@api_view(['GET', 'POST'])
#def song_list(request, format=None):
#    """
#    List all code snippets, or create a new snippet.
#    """
#    if request.method == 'GET':
#        songs = Song.objects.all()
#        serializer = SongSerializer(songs, many=True)
#        return Response(serializer.data)
#
#    elif request.method == 'POST':
#        
#        serializer = SongSerializer(data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data, status=status.HTTP_201_CREATED)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
#@api_view(['GET', 'PUT', 'DELETE'])
#def song_detail(request, pk, format=None):
#    """
#    Retrieve, update or delete a code snippet.
#    """
#    try:
#        song = Song.objects.get(pk=pk)
#    except Song.DoesNotExist:
#        return Response(status=status.HTTP_404_NOT_FOUND)
#
#    if request.method == 'GET':
#        serializer = SongSerializer(song)
#        return Response(serializer.data)
#
#    elif request.method == 'PUT':
#        serializer = SongSerializer(song, data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data)
##        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
##
##    elif request.method == 'DELETE':
##        song.delete()
##        return Response(status=status.HTTP_204_NO_CONTENT)
#
#class AlbumList(APIView):
#    """
#    List all snippets, or create a new snippet.
#    """
#    def get(self, request, format=None):
#        album = Album.objects.all()
#        serializer = AlbumSerializer(salbum, many=True)
#        return Response(serializer.data)
#
#    def post(self, request, format=None):
#        serializer = AlbumSerializer(data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data, status=status.HTTP_201_CREATED)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#class AlbumDetail(APIView):
#    """
#    Retrieve, update or delete a snippet instance.
#    """
#    def get_object(self, pk):
#        try:
#            return Album.objects.get(pk=pk)
#        except Album.DoesNotExist:
#            raise Http404
#
#    def get(self, request, pk, format=None):
#        album = self.get_object(pk)
#        serializer = SnippetSerializer(album)
#        return Response(serializer.data)
#
#    def put(self, request, pk, format=None):
#        album = self.get_object(pk)
#        serializer = AlbumSerializer(album, data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#    def delete(self, request, pk, format=None):
#        album = self.get_object(pk)
#        album.delete()
#        return Response(status=status.HTTP_204_NO_CONTENT)












#@api_view(['GET', 'POST'])
#def Album_list(request, format=None):
#    """
#    List all code snippets, or create a new snippet.
#    """
#    if request.method == 'GET':
#        albums = Album.objects.all()
#        serializer = AlbumSerializer(albums, many=True)
#        return Response(serializer.data)
#
#    elif request.method == 'POST':
#        
#        serializer = AlbumSerializer(data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data, status=status.HTTP_201_CREATED)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#@api_view(['GET', 'PUT', 'DELETE'])
#def Album_detail(request, pk, format=None):
#    """
#    Retrieve, update or delete a code snippet.
#    """
#    try:
#        album = Album.objects.get(pk=pk)
#    except Album.DoesNotExist:
#        return Response(status=status.HTTP_404_NOT_FOUND)
#
#    if request.method == 'GET':
#        serializer = AlbumSerializer(album)
#        return Response(serializer.data)
#
#    elif request.method == 'PUT':
#        data = JSONParser().parse(request)
#        serializer = AlbumSerializer(album, data=drequest.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#    elif request.method == 'DELETE':
#        Album.delete()
#        return Response(status=status.HTTP_204_NO_CONTENT)