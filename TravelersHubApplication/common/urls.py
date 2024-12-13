from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('all-trips/', views.all_trips, name='all-trips'),
]
