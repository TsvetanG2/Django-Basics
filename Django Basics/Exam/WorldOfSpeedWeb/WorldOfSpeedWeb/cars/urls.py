from django.urls import path, include

from WorldOfSpeedWeb.cars.views import (CreateCarView,
                                        DetailCarView,
                                        EditCarView,
                                        DeleteCarView)

from WorldOfSpeedWeb.web.views import index_with_profile

urlpatterns = (
    path('catalogue/', index_with_profile, name='catalogue'),
    path('create/', CreateCarView.as_view(), name='create_car'),
    path('<int:pk>/',
         include([
             path('details/', DetailCarView.as_view(), name='details_car'),
             path('edit/', EditCarView.as_view(), name='edit_car'),
             path('delete/', DeleteCarView.as_view(), name='delete_car'),
         ])
     ),
)
