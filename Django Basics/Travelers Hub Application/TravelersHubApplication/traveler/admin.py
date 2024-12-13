from django.contrib import admin

from .models import Traveler

# Register your models here.
@admin.register(Traveler)
class TravelerAdmin(admin.ModelAdmin):
    pass
