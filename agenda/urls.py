from django.urls import path
from agenda import views


app_name = 'agenda'


urlpatterns = [
    path('', views.ListViewHome.as_view(), name='home'),
    path('view_contact/<int:pk>/',
         views.DetalViewContact.as_view(),
         name='view_contact'
         ),

    path('add_contact/', views.AddUpdateContact.as_view(), name='add_contact'),
    path('add_category/',
         views.AddCategoryView.as_view(),
         name='add_category'
         ),

    path('remove_contact/<int:id>/',
         views.RemoveContactView.as_view(),
         name='remove_contact'
         ),
    path('remove_category/',
         views.RemoveCategoryView.as_view(),
         name='remove_category'
         ),

    path('update_contact/<int:id>/',
         views.AddUpdateContact.as_view(),
         name='update_contact'
         ),
    path('update_category/',
         views.UpdateCategoryView.as_view(),
         name='update_category'
         ),

    path('search/', views.ListViewSearch.as_view(), name='search'),
]
