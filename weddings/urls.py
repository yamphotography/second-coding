from unicodedata import name
from django.contrib import admin
from django.urls import path, include
from .views import *




   
urlpatterns = [
    path('', weddings, name='weddings'),
    path('wedding/<str:pk>/',wedding, name="wedding"),
    path('create-wedding/',createWedding, name="create-wedding"),
    path('update-wedding/<str:pk>/', updateWedding, name="update-wedding"),
    path('delete-wedding/<str:pk>/', deleteWedding, name="delete-wedding"),
    path('users', include('users.urls')),
]
   
