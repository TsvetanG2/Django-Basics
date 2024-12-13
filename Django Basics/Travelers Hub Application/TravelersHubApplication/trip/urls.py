from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_trip, name='create-trip'),
    path('<int:trip_id>/edit/', views.edit_trip, name='edit-trip'),
    path('<int:trip_id>/delete/', views.delete_trip, name='delete-trip'),
    path('<int:trip_id>/details/', views.details_trip, name='details-trip'),
]
