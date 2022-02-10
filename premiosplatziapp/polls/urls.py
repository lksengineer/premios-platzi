# Django
from django.urls import path

# Views
from . import views

# Create your URLS here.
urlpatterns = [
    path('', views.index, name='index'),
]