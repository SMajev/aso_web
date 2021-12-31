from django.urls import path
from .views import Index, Services, EventCreateView, AboutView



urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('services', Services.as_view(), name='services'),
    path('event/create', EventCreateView.as_view(), name='event-create')
]
