from django.conf.urls import url
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('accom/', views.accom, name='accommodation'),
    path('contact/', views.contact, name='contact'),
    path('guest-book/', views.book, name='guest-book')
]
