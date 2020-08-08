from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home-page'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('contact/', views.portfolio, name='portfolio'),
]