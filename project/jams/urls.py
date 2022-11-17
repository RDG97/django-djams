from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from jams import views

urlpatterns = [
    path('Genres/', views.GenreList.as_view()),
    path('Genres/<int:pk>/', views.GenreDetail.as_view()),

    path('Artists/', views.ArtistList.as_view()),
    path('Artists/<int:pk>/', views.ArtistDetail.as_view()),

    path('Albums/', views.AlbumList.as_view()),
    path('Albums/<int:pk>/', views.AlbumDetail.as_view()),

    path('Songs/', views.SongList.as_view()),
    path('Songs/<int:pk>/', views.SongDetail.as_view()),

    path('Playlists/', views.PlaylistList.as_view()),
    path('Playlists/<int:pk>/', views.PlaylistDetail.as_view()),
    path('PlaylistSongs/', views.PlaylistSongList.as_view()),
    path('PlaylistSongs/<int:pk>', views.PlaylistSongDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)