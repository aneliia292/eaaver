from django.urls import path
from .views import index, about, contacts, client, clientsView

urlpatterns = [
    path('',index, name='home'),
    path('about', about, name='about'),
    path('contacts', contacts, name='contacts'),
    path('user/<int:id>', client, name='client'),
    path('users', clientsView, name='clients')
]