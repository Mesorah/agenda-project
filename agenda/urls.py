from django.urls import path
from rest_framework.routers import SimpleRouter

from agenda import views

app_name = 'agenda'

contact_api_router = SimpleRouter()
contact_api_router.register(
    'api',
    views.ContactAPIViewSet,
    basename='api'
)


urlpatterns = [
     path('', views.ListViewHome.as_view(), name='home'),
     path(
          'view_contact/<int:pk>/',
          views.DetalViewContact.as_view(),
          name='view_contact'
          ),

     path(
          'add_contact/',
          views.ContactCreateView.as_view(),
          name='add_contact'
          ),
     path(
          'update_contact/<int:pk>/',
          views.ContactUpdateView.as_view(),
          name='update_contact'
          ),
     path(
          'remove_contact/<int:pk>/',
          views.ContactDeleteView.as_view(),
          name='remove_contact'
          ),

     path(
          'add_category/',
          views.CategoryCreateView.as_view(),
          name='add_category'
          ),
     path(
          'remove_category/',
          views.CategoryDeleteView.as_view(),
          name='remove_category'
          ),
     path(
          'update_category/',
          views.CategoryUpdateView.as_view(),
          name='update_category'
          ),

     path('search/', views.ListViewSearch.as_view(), name='search'),

     # path(
     #      'api/',
     #      views.ContactAPIViewSet.as_view(),
     #      name='contact_api'
     #      ),

     # path(
     #      'api/<int:pk>/',
     #      views.ContactAPIViewSet.as_view(),
     #      name='contact_api_detail'
     #      ),

     path(
          'api/category/<int:pk>/',
          views.CategoryAPIDetailView.as_view(),
          name='category_api_detail'
          ),
]

urlpatterns += contact_api_router.urls
