from django import forms
from django.shortcuts import render, redirect

from ExamPreparationApp.albums.models import Album
from ExamPreparationApp.profiles.models import Profile


def get_profile():
    return Profile.objects.first()
    # If this profile exists we cannot create it


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'email', 'age']

        widgets = {
            'username': forms.TextInput(
                attrs={
                    'placeholder': 'Username'
                },
            ),
            'email': forms.TextInput(
                attrs={
                    'placeholder': 'Email'
                },
            ),
            'age': forms.TextInput(
                attrs={
                    'placeholder': 'Age'
                },
            ),
        }

def create_profile(request):
    form = CreateProfileForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("index")

    context = {
        'form': form,
        'no_nav': True,
    }
    return render(request, "web/home-no-profile.html", context)


def index_with_profile(request):

    context = {
        'albums': Album.objects.all(),
    }

    return render(request, "web/home-with-profile.html", context)


def index(request):
    profile = get_profile()

    if profile is None:
        return create_profile(request)

    return index_with_profile(request)


