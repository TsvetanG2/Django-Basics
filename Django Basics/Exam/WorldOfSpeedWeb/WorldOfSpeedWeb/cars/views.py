from django.forms import modelform_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from WorldOfSpeedWeb.cars.models import Car
from WorldOfSpeedWeb.web.views import get_profile


class FormMixin():
    # Another way to create widgets, check web.views for simplier way
    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)

        form.fields['type'].widget.attrs['placeholder'] = 'Type'
        form.fields['model'].widget.attrs['placeholder'] = 'Model'
        form.fields['year'].widget.attrs['placeholder'] = 'Year'
        form.fields['image_url'].widget.attrs['placeholder'] = 'Image URL'
        form.fields['price'].widget.attrs['placeholder'] = 'Price'

        return form


class ReadOnlyMixin:
    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)

        for field in form.fields.values():
            field.widget.attrs['readonly'] = 'readonly'

        return form


class CreateCarView(FormMixin, views.CreateView):
    queryset = Car.objects.all()
    fields = ('type',
              'model',
              'year',
              'image_url',
              'price',
              )
    template_name = 'cars/car-create.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        # TODO: Check for better solution
        instance = form.save(commit=False)
        instance.owner = get_profile()
        return super().form_valid(form)


class DetailCarView(views.DetailView):
    queryset = Car.objects.all()
    template_name = 'cars/car-details.html'


class EditCarView(FormMixin, views.UpdateView):
    queryset = Car.objects.all()
    template_name = 'cars/car-edit.html'
    fields = ('type',
              'model',
              'year',
              'image_url',
              'price',
              )
    success_url = reverse_lazy('index')


class DeleteCarView(ReadOnlyMixin, views.DeleteView):
    queryset = Car.objects.all()
    template_name = 'cars/car-delete.html'
    success_url = reverse_lazy('index')

    form_class = modelform_factory(Car,
                                   fields=('type',
                                           'model',
                                           'year',
                                           'image_url',
                                           'price',
                                           )
                                   )

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.object
        return kwargs
