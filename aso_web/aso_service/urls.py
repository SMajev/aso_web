from django.urls import path
from .views import (
    Index, Services, EventDetail, EventCreate, AboutView,
    CustomerEventsList, MechanicEventsList
)



urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('services', Services.as_view(), name='services'),
    path('event/<int:pk>', EventDetail.as_view(), name='event-detail'),
    path('events', CustomerEventsList.as_view(), name='events'),
    path('mevents', MechanicEventsList.as_view(), name='mevents'),
    path('event/create', EventCreate.as_view(), name='event-create'),
]
