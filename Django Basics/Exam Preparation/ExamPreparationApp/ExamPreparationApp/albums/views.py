from django.forms import modelform_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from ExamPreparationApp.albums.models import Album
from ExamPreparationApp.web.views import get_profile


class FormMixin():
    # Another way to create widgets, check web.views for simplier way
    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)

        form.fields['album_name'].widget.attrs['placeholder'] = 'Album Name'
        form.fields['artist'].widget.attrs['placeholder'] = 'Artist'
        form.fields['image_url'].widget.attrs['placeholder'] = 'Image URL'
        form.fields['price'].widget.attrs['placeholder'] = 'Price'

        return form


class ReadOnlyMixin:
    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)

        for field in form.fields.values():
            field.widget.attrs['readonly'] = 'readonly'

        return form




class CreateAlbumView(FormMixin, views.CreateView):
    queryset = Album.objects.all()
    fields = ('album_name',
              'artist',
              'genre',
              'description',
              'image_url',
              'price'
              )
    template_name = 'albums/album-add.html'
    success_url = reverse_lazy('index')


    def form_valid(self, form):
        # TODO: Check for better solution
        instance = form.save(commit=False)
        instance.owner = get_profile()
        return super().form_valid(form)


class DetailAlbumView(views.DetailView):
    queryset = Album.objects.all()
    template_name = 'albums/album-details.html'


class EditAlbumView(FormMixin, views.UpdateView):
    queryset = Album.objects.all()
    template_name = 'albums/album-edit.html'
    fields = ('album_name',
              'artist',
              'genre',
              'description',
              'image_url',
              'price'
              )
    success_url = reverse_lazy('index')

class DeleteAlbumView(ReadOnlyMixin, views.DeleteView):
    queryset = Album.objects.all()
    template_name = 'albums/album-delete.html'
    success_url = reverse_lazy('index')

    form_class = modelform_factory(Album,
        fields=('album_name',
               'artist',
               'genre',
               'description',
               'image_url',
               'price'
               )
       )

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.object
        return kwargs

    #def form_valid(self, form):
        #form.instance = self.object
        #return super().form_valid(form=form)

