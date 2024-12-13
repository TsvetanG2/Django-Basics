from django.shortcuts import render, redirect, get_object_or_404
from .forms import TravelerForm
from .models import Traveler
from ..trip.models import Trip


def create_traveler(request):
    if request.method == 'POST':
        form = TravelerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TravelerForm()
    return render(request, 'create-traveler.html', {'form': form})

def edit_traveler(request, traveler_id):
    traveler = Traveler.objects.get(id=traveler_id)
    if request.method == 'POST':
        form = TravelerForm(request.POST, instance=traveler)
        if form.is_valid():
            form.save()
            return redirect('details-traveler', traveler_id=traveler.id)
    else:
        form = TravelerForm(instance=traveler)
    return render(request, 'edit-traveler.html', {'form': form})


def details_traveler(request, traveler_id):
    traveler = get_object_or_404(Traveler, id=traveler_id)
    trips = Trip.objects.filter(traveler=traveler).order_by('-start_date')

    return render(request, 'details-traveler.html', {
        'traveler': traveler,
        'trips': trips,
        'traveler_id': traveler.id,
    })


def delete_traveler(request, traveler_id):
    traveler = get_object_or_404(Traveler, id=traveler_id)

    if request.method == 'POST':
        print(f"Deleting traveler with ID {traveler_id}")
        traveler.trips.all().delete()
        traveler.delete()
        print("Traveler and trips deleted.")
        return redirect('index')

    return render(request, 'delete-traveler.html', {'traveler': traveler})

