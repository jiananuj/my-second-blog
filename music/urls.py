from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
    # / music /
    url(r'^$', views.IndexView.as_view(),name='index'),

    url(r'^register/$', views.UserFormView.as_view(), name='register'),

    # / music/artist /
    url(r'^(?P<id>\w+)/$', views.AlbumView.as_view(), name='songalbum'),

    # /music/artist/<album_id>/
    url(r'^(?P<album>\w+)/(?P<id>\w+)/$', views.DetailView.as_view() , name='detail'),

    # /music/<album_id>/favorite/
    url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),


    # /music/album/add/
    url(r'album/add/$', views.AlbumCreate.as_view(), name='album-add'),

    # /music/album/2(update)/
    url(r'album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='album-update'),

    # /music/album/2/delete4
    url(r'album/(?P<id>\w+)/delete/', views.AlbumDelete.as_view(), name='album-delete'),
]