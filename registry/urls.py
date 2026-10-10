from django.urls import path
from registry import views

urlpatterns = [
    path('', views.registry_home, name='home'),
    path('submit/', views.submit_resource, name='submit'),
]
