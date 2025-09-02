from django.urls import path
from . import views


urlpatterns = [
   path('welcome/',views.welcome.as_view(),name='welcome')
]
