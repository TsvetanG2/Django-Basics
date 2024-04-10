from django.urls import path, include

from WorldOfSpeedWeb.web.views import create_profile
from WorldOfSpeedWeb.profiles.views import DeleteProfileView, DetailProfileView, EditProfileView


urlpatterns = (
    path('create/', create_profile, name='create_profile'),
    path('details/', DetailProfileView.as_view(), name='profile_details'),
    path('<int:pk>/', include([
        path('delete/', DeleteProfileView.as_view(), name='delete_profile'),
        path('edit/', EditProfileView.as_view(), name='edit_profile'),

            ]
        ),
    )
)