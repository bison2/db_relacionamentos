from django.contrib import admin
from django.urls import path
from ManyToApp import views

urlpatterns =[
    path('admin/', admin.site.urls),
    path('', views.home),
]