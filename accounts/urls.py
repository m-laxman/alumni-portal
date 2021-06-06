from django.contrib import admin
from django.urls import path
from accounts import views
from django.conf import settings

urlpatterns = [
    path("register/", views.register, name='register'),
    path("login/", views.login, name='login'),
    path("logout/", views.logout, name='logout'),
    path("profile/", views.profile, name='logout'),
    path("editprofile/", views.editprofile, name="editprofile")

]
