from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('ExamPreparationApp.web.urls')),
    path('profile/', include('ExamPreparationApp.profiles.urls')),
    path('album/', include('ExamPreparationApp.albums.urls')),
]
