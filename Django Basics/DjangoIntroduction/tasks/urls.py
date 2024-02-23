#Do awlays when creating new Django App:

#(Optional) Move to project directory
#Create 'urls.py' file
#Register this Django app's 'urls.py' in the project's 'urls'py file
#Register this Django app in 'settings.py' INSTALLED_APPS

from django.urls import path
from .views import index

urlpatterns = (
    path("", index),

)
