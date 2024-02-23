from django.urls import reverse_lazy
from django.views import generic as views

from ExamPreparationApp.profiles.models import Profile


def get_profile():
    return Profile.objects.first()
    # If this profile exists we cannot create it


class DetailProfileView(views.DetailView):
    queryset = Profile.objects.all()
    template_name = 'profile/profile-details.html'

    def get_object(self, queryset=None):
        return get_profile()


class DeleteProfileView(views.DeleteView):
    template_name = 'profile/profile-delete.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        return get_profile()


