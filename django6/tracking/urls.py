from django.urls import path,include
from . import views


app_name = 'tracking'

urlpatterns = [
    path('home/',views.Home.as_view(),name='Home'),
    path('',include('tracking.tests.urls')),
    
]