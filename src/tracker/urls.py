"""tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
# from django.contrib import admin
from django.urls import path

from tracker import views

urlpatterns = [
    path(r'', views.entrypoint, name='entrypoint'),
    path(r'route/', views.route, name='route'),
    path(r'route/<int:route_id>/', views.delete_route, name='delete_route'),
    path(r'route/<int:route_id>/way_point/', views.way_point, name='way_point'),
    path(r'route/<int:route_id>/length/', views.length, name='length'),
    path(r'route/longest/<str:date>/', views.longest_route, name='longest_route'),
]
