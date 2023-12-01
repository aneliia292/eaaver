from django.urls import path
from .views import index, about, contacts, form

urlpatterns = [
    path('', index, name='home'),
    path('about', about, name='about'),
    path('contacts', contacts, name='contacts'),
    path('registrate/', form, name='registrate'),
]