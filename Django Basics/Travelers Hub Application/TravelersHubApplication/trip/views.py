from django.shortcuts import render, redirect, get_object_or_404
from .forms import TripForm
from .models import Trip
from ..common.views import get_profile


def create_trip(request):
    traveler = get_profile()

    if not traveler:
        return redirect('create-traveler')

    if request.method == 'POST':
        form = TripForm(request.POST)
        if form.is_valid():

            trip = form.save(commit=False)
            trip.traveler = traveler
            trip.save()

            return redirect('all-trips')
    else:
        form = TripForm()

    return render(request, 'create-trip.html', {'form': form, 'traveler': traveler})


def edit_trip(request, trip_id):
    traveler = get_profile()

    if not traveler:
        return redirect('create-traveler')

    trip = get_object_or_404(Trip, id=trip_id)

    if request.method == 'POST':
        form = TripForm(request.POST, instance=trip)
        if form.is_valid():
            form.save()
            return redirect('all-trips')

    else:
        form = TripForm(instance=trip)

    context = {
        'form': form,
        'traveler': traveler,
    }

    return render(request, 'edit-trip.html', context)

def delete_trip(request, trip_id):
    traveler = get_profile()

    if not traveler:
        return redirect('create-traveler')

    trip = get_object_or_404(Trip, id=trip_id)

    if request.method == 'POST':
        trip.delete()  # Delete the trip
        return redirect('all-trips')

    return render(request, 'delete-trip.html', {'trip': trip, 'traveler': traveler})


def details_trip(request, trip_id):
    traveler = get_profile()

    if not traveler:
        return redirect('create-traveler')

    trip = get_object_or_404(Trip, id=trip_id)

    return render(request, 'details-trip.html', {'trip': trip, 'traveler': traveler})
