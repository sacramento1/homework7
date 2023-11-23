from django.urls import path
from .views import main

urlpatterns = [
    path('main/', main, name='main'),
    # path('post/<str:pk>', detail, name='detail')
]
