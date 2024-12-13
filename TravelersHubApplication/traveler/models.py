from django.db import models
from django.core.exceptions import ValidationError
import re

def validate_nickname(value):
    if not re.match(r'^[a-zA-Z0-9]+$', value):
        raise ValidationError('Your nickname is invalid!')

class Traveler(models.Model):
    nickname = models.CharField(
        max_length=30,
        unique=True,
        validators=[validate_nickname],
        help_text="Nicknames can contain only letters and digits."
    )
    email = models.EmailField(
        max_length=30,
        unique=True
    )
    country = models.CharField(
        max_length=3
    )
    about_me = models.TextField(
        blank=True
    )

    def __str__(self):
        return self.nickname
