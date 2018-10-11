from django.urls import path

from . import views

urlpatterns = [
   path('', views.Name, name='Name'),
    path('school/', views.School, name="School"),
    path('hour/', views.Hour, name="Hour"),
    path('dateofwork/', views.DateofWork, name="DateofWork"),
    path('dateofentry/', views.DateofEntry, name="DateEntry"),

]