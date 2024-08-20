from django.urls import path
from authors import views


app_name = 'authors'


urlpatterns = [
    path('register_author/', views.register_author, name='register_author'),
    path('login_author/', views.login_author, name='login_author'),
    path('logout_author/', views.logout_author, name='logout_author'),
]
