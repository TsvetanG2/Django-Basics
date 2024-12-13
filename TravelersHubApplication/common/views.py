from django.shortcuts import render, redirect
from TravelersHubApplication.traveler.models import Traveler
from TravelersHubApplication.trip.models import Trip

def get_profile():
    return Traveler.objects.first()

def index_with_profile(request):
    traveler = get_profile()

    if traveler:
        trips = Trip.objects.filter(traveler=traveler).order_by('-start_date')
        context = {
            'traveler': traveler,
            'trips': trips,
        }
        return render(request, "index.html", context)

    return redirect('index')


def index(request):
    traveler = get_profile()

    if traveler is None:
        return render(request, 'index.html', {'traveler': None})

    return index_with_profile(request)

def all_trips(request):
    traveler = get_profile()

    if traveler:
        trips = Trip.objects.filter(traveler=traveler).order_by('-start_date')
        context = {
            'traveler': traveler,
            'trips': trips,
        }
        return render(request, "all-trips.html", context)

    return redirect('index')