from django import forms
from django.shortcuts import render, redirect

from WorldOfSpeedWeb.cars.models import Car
from WorldOfSpeedWeb.profiles.models import Profile


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'email', 'age', 'password']
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
            'password': forms.PasswordInput(
                attrs={
                    'data-mask': ''
                }
            )

        }


def get_profile():
    return Profile.objects.first()


def create_profile(request):
    form = CreateProfileForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("catalogue")

    context = {
        'form': form,
        'no_nav': True,
    }
    return render(request, "profiles/profile-create.html", context)


def index_with_profile(request):
    context = {
        'cars': Car.objects.all(),
    }

    return render(request, "web/catalogue.html", context)


def index(request):
    profile = get_profile()

    if profile is None:
        return create_profile(request)

    return index_with_profile(request)