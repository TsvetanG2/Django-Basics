from django.db import models
from django.utils import timezone
from TravelersHubApplication.traveler.models import Traveler

class Trip(models.Model):
    destination = models.CharField(
        max_length=100
    )
    summary = models.TextField()
    start_date = models.DateField(
        default=timezone.now
    )
    duration = models.PositiveSmallIntegerField(
        default=1,
        help_text="Duration in days is expected."
    )
    image_url = models.URLField(
        blank=True
    )
    traveler = models.ForeignKey(
        Traveler, on_delete=models.CASCADE,
        related_name='trips'
    )

    def __str__(self):
        return f"{self.destination} - {self.start_date}"
