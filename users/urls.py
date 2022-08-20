from django.urls import path

from .views import *

urlpatterns = [

path('', profiles, name="profiles"),
path('profile/<str:pk>/',userprofile, name="profile"),
path('login/',loginPage, name="login"),
path('logout/',logOutUser, name="logout"),
path('register/',registerUser, name="register"),
path('account/',userAccount, name="account"),
path('edit_account/',editAccount, name="edit-account"),
path('messages/',inbox, name="messages"),
path('skill-create/',createSkill, name="skill-create"),

]