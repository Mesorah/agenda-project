from django.urls import path
from agenda import views


app_name = 'agenda'


urlpatterns = [
    path('', views.home, name='home'),
    path('add_contact', views.add_contact, name='add_contact'),
    path('view_contact/<int:id>/', views.view_contact, name='view_contact'),
    path('remove_contact/<int:id>/', views.remove_contact, name='remove_contact'), # noqa E501
    path('update_contact/<int:id>/', views.update_contact, name='update_contact'), # noqa E501
]
