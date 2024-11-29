from django.urls import path
from authors import views


app_name = 'authors'


urlpatterns = [
    path('register_author/',
         views.AuthorRegisterView.as_view(),
         name='register_author'
         ),
    path('login_author/',
         views.AuthorLoginView.as_view(),
         name='login_author'
         ),
    path('logout_author/',
         views.AuthorLogoutView.as_view(),
         name='logout_author'
         ),
]
