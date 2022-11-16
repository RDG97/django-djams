from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from jams import views

urlpatterns = [
    path('songs/', views.SongList.as_view()),
    path('songs/<int:pk>/', views.SongDetail.as_view()),
    path('albums/', views.AlbumList.as_view()),
    path('albums/<int:pk>/', views.AlbumDetail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)