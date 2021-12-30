from django.urls import path
from .views import Index, Services



urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('services', Services.as_view(), name='services'),
    
]
