from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_traveler, name='create-traveler'),
    path('edit/<int:traveler_id>/', views.edit_traveler, name='edit-traveler'),
    path('details/<int:traveler_id>/', views.details_traveler, name='details-traveler'),
    path('delete/<int:traveler_id>/', views.delete_traveler, name='delete-traveler'),
]
