from django.urls import path

from WorldOfSpeedWeb.web.views import index, index_with_profile

urlpatterns = [
    path('', index, name='index'),
    path('', index_with_profile, name='index_profile')
]