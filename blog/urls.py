"""
URL configuration for website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.index, name="index"),
    path("post/<str:id>", views.post, name="post"),
    path("about/", views.about, name="about"),
    path("services/", views.services, name="services"),
    path("contact/", views.contacts, name="contact"),
    path("category/<str:name>", views.category, name="category"),
    path("search", views.search, name="search"),
    path("create", views.create, name="create"),
    path("login", LoginView.as_view(), name="blog_login"),
    path("logout", LogoutView.as_view(), name="blog_logout"),
    path('register/', views.sign_up, name='register'),
]
