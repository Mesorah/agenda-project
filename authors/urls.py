from django.urls import path
from authors import views


app_name = 'authors'


urlpatterns = [
    path('register_author/',
         views.RegisterAuthorView.as_view(),
         name='register_author'
         ),
    path('login_author/',
         views.LoginAuthorView.as_view(),
         name='login_author'
         ),
    path('logout_author/',
         views.LogoutAuthorView.as_view(),
         name='logout_author'
         ),
]
