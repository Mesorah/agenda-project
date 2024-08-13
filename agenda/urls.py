from django.urls import path
from agenda import views


app_name = 'agenda'


urlpatterns = [
    path('', views.home, name='home'),
]
