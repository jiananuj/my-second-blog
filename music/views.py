
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm

from .models import Album, Song, Artists



class IndexView(generic.ListView):
    template_name = 'music/index.html'

    def get_queryset(self):
        return Artists.objects.all()

class AlbumView(generic.DetailView):
    template_name = 'music/album.html'
    model = Artists
    def get_queryset(self):
        return Album.objects.all()

#AttributeError: Generic detail view DetailView must be called with either an object pk or a slug.
    def get_object(self):
        object = get_object_or_404(Artists, id=self.kwargs['id'])
        return object

class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'

    def get_object(self):
        object = get_object_or_404(Album , id=self.kwargs['id'])
        return object


def favorite(request, album_id):
        album = get_object_or_404(Album, pk=album_id)
        try:
            selected_song = album.song_set.get(pk=request.POST['song'])

        except (KeyError, Song.DoesNotExist):
            return render(request, 'music/detail.html', {
                'album': album,
                'error_message': "not a valid song",
            })
        else:
            selected_song.is_favorite = True
            selected_song.save()
            return render(request, 'music/detail.html', {'album': album})


class AlbumCreate(CreateView):
    model = Album
    fields = ['artist' , 'album_title' , 'genre' , 'album_logo']
   # template_name = 'music/album_form.html'


class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist' , 'album_title' , 'genre' , 'album_logo']

class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:songalbum')

    def get_object(self):
        object = get_object_or_404(Album , id=self.kwargs['id'])
        return object


class UserFormView(View):
    form_class = UserForm
    template_name = 'music/registration_form.html'

    # display a blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            # cleaned (normalised) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            #returns User objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('music:index')

        return render(request, self.template_name, {'form': form})
