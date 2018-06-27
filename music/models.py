from django.db import models
from django.urls import reverse


class Artists(models.Model):
    name = models.CharField(max_length=250)
    type = models.CharField(max_length=250)
    nation = models.CharField(max_length=250)
    artist_logo = models.CharField(max_length=1000)

    def get_absolute_url(self):
        return reverse('music:songalbum', kwargs={'pkArtist': self.pk})

    def __str__ (self):
        return self.name

class Album(models.Model):
    artist = models.ForeignKey(Artists, on_delete=models.CASCADE)
    album_title = models.CharField(max_length=250)
    genre = models.CharField(max_length=250)
    album_logo = models.CharField(max_length=1000)



    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pkAlbum': self.pk})


    def __str__ (self):
        return self.album_title

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)
    is_favorite = models.BooleanField(default=False)

    def __str__ (self):
        return self.song_title


