from django.urls import reverse_lazy
from django.views import generic as views

from WorldOfSpeedWeb.profiles.models import Profile


def get_profile():
    return Profile.objects.first()
    # If this profile exists we cannot create it


class DetailProfileView(views.DetailView):
    queryset = Profile.objects.all()
    template_name = 'profiles/profile-details.html'

    def get_object(self, queryset=None):
        return get_profile()


class DeleteProfileView(views.DeleteView):
    template_name = 'profiles/profile-delete.html'
    success_url = reverse_lazy('index_profile')

    def get_object(self, queryset=None):
        return get_profile()


class EditProfileView(views.UpdateView):
    queryset = Profile.objects.all()
    template_name = 'profiles/profile-edit.html'
    fields = ('username',
              'email',
              'age',
              'password',
              'first_name',
              'last_name',
              'profile_picture',
              )
    success_url = reverse_lazy('profile_details')

