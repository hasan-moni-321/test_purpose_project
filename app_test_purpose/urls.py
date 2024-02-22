from django.urls import path 
from app_test_purpose import views 

urlpatterns = [
    path('', views.index, name='index'), 
]
