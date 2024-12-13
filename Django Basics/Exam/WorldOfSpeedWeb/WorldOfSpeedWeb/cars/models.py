from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models
from WorldOfSpeedWeb.profiles.models import Profile


def validate_year(year):
    if not 1999 < year < 2030:
        raise ValidationError("Year must be between 1999 and 2030!")


class Car(models.Model):

    MIN_PRICE_VALUE = 1.0

    CAR_CHOICES = (
        ('RALLY', 'Rally'),
        ('OPEN-WHEEL', 'Open-wheel'),
        ('KART', 'Kart'),
        ('DRAG', 'Drag'),
        ('OTHER', 'Other'),
    )

    type = models.CharField(
        blank=False,
        null=False,
        max_length=10,
        choices=CAR_CHOICES,
        verbose_name='Type',
    )
    model = models.CharField(
        blank=False,
        null=False,
        max_length=15,
        validators=[
            MinLengthValidator(1),
        ],
        verbose_name='Model',
    )
    year = models.IntegerField(
        blank=False,
        null=False,
        verbose_name='Year',

    )
    image_url = models.URLField(
        blank=False,
        null=False,
        unique=True,
        error_messages={
            'unique': "This image URL is already in use! Provide a new one."
        },
        default='https://...',
        verbose_name='Image URL',
    )
    price = models.FloatField(
        blank=False,
        null=False,
        validators=[
            MinValueValidator(MIN_PRICE_VALUE)
        ],
        verbose_name='Price',
    )
    owner = models.ForeignKey(
        to=Profile,
        on_delete=models.CASCADE,
        editable=False,
    )


