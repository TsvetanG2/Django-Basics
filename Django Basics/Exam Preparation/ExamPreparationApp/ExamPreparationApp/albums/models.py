from django.core.validators import MinValueValidator
from django.db import models

from ExamPreparationApp.profiles.models import Profile

"""· Album

o Album Name
    Character field, required.
    All album names must be unique.
    It should consist of a maximum of 30 characters.

o Artist
    Character field, required.
    It should consist of a maximum of 30 characters.

o Genre
    Character field, required.
    It should consist of a maximum of 30 characters.
    The choices are "Pop Music", "Jazz Music", "R&B Music", "Rock Music", "Country Music", "Dance Music", "Hip Hop Music", and "Other".

o Description
    Text field, optional.

o Image URL
    URL field, required.

o Price
    Float field, required.
    The price cannot be below 0.0.

o Owner
    A foreign key to the Profile model.
    Establishes a many-to-one relationship with the Profile model, associating each album with a profile.
    The ON DELETE constraint must be configured to an appropriate value in alignment with the specified additional tasks.
    This field should remain hidden in forms."""


class Album(models.Model):
    MAX_AlBUM_NAME = 30
    MAX_ARTIST_NAME = 30
    MAX_GENRE_NAME = 30

    MIN_PRICE = 0.0

    GENRE_CHOICES = (
        ("JAZZ MUSIC", "Jazz Music"),
        ("R&B MUSIC", "R&B Music"),
        ("ROCK MUSIC", "Rock Music"),
        ("COUNTRY MUSIC", "Country Music"),
        ("DANCE MUSIC", "Dance Music"),
        ("HIP HOP MUSIC", "Hip Hop Music"),
        ("OTHER", "Other"),

    )
    album_name = models.CharField(
        unique=True,
        max_length=MAX_AlBUM_NAME,
        null=False,
        blank=False,
        verbose_name='Album Name',
    )
    artist = models.CharField(
        max_length=MAX_ARTIST_NAME,
        null=False,
        blank=False,
        verbose_name='Artist',
    )
    genre = models.CharField(
        max_length=MAX_GENRE_NAME,
        null=False,
        blank=False,
        choices=GENRE_CHOICES,
        verbose_name='Genre',
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name='Description',
    )
    image_url = models.URLField(
        null=False,
        blank=False,
        verbose_name='Image URL',
    )
    price = models.FloatField(
        null=False,
        blank=False,
        validators=(
            MinValueValidator(MIN_PRICE),
        )
    )
    owner = models.ForeignKey(
        to=Profile,
        on_delete=models.CASCADE,
        editable=False,
    )



