from django.urls import path
from authors import views


app_name = 'authors'


urlpatterns = [
    path('register_author/', views.register_author, name='register_author'),
]
