from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models

"""
· Profile

o Username
    Character field, required.
    It should have at least 2 characters and maximum - 15 characters.
    The username can consist only of letters, numbers, and underscore ("_"). Otherwise, raise a ValidationError with the message: "Ensure this value contains only letters, numbers, and underscore."

o Email
    Email field, required.

o Age
    Integer field, optional.
    The age cannot be below 0"""


def validate_username(username):
    is_valid = all(ch.isalnum or ch == '_' for ch in username)

    if not is_valid:
        raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")


class Profile(models.Model):
    MIN_USERNAME_LENGTH = 2
    MAX_USERNAME_LENGTH = 15
    username = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_USERNAME_LENGTH,
        validators=(
            MinLengthValidator(MIN_USERNAME_LENGTH),
        )
    )
    email = models.EmailField(
        null=False,
        blank=False,
    )
    age = models.IntegerField(
        null=False,
        blank=False
    )
