from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MinLengthValidator
from django.db import models
from django import forms


def validate_lenght_username(username):
    if username < len(username) == 3:
        raise ValidationError("Username must be at least 3 chars long!")


def validate_username(username):
    is_valid = all(ch.isalnum or ch == '_' for ch in username)

    if not is_valid:
        raise ValidationError("Username must contain only letters, digits, and underscores!")


class Profile(models.Model):
    MAX_CHAR_USERNAME = 15
    MIN_CHAR_USERNAME = 3

    username = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_CHAR_USERNAME,
        validators=[
            MinLengthValidator(MIN_CHAR_USERNAME)
        ],
        verbose_name='Username',

    )
    email = models.EmailField(
        null=False,
        blank=False,
    )
    age = models.IntegerField(
        null=False,
        blank=False,
        validators=[
            MinValueValidator(21)
        ],
        help_text='Age requirement: 21 years and above.',
        verbose_name='Age',
    )
    password = models.CharField(
        null=False,
        blank=False,
        max_length=20,
        verbose_name='Password',
    )
    first_name = models.CharField(
        max_length=25,
        blank=True,
        verbose_name='First Name',
    )
    last_name = models.CharField(
        max_length=25,
        blank=True,
        null=False,
        verbose_name='Last Name',
    )
    profile_picture = models.URLField(
        verbose_name='Profile Picture',
        blank=True,
        null=False,
    )

