from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_numbers, name='get_numbers'),
]
