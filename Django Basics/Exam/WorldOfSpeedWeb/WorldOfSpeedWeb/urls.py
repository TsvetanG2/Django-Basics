from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('WorldOfSpeedWeb.web.urls')),
    path('car/', include('WorldOfSpeedWeb.cars.urls')),
    path('profile/', include('WorldOfSpeedWeb.profiles.urls')),
]
