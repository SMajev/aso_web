from django.urls import path
from .views import *


urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('services', Services.as_view(), name='services'),

    path('event/<int:pk>', EventDetail.as_view(), name='event-detail'),
    path('myevents', CustomerEventsList.as_view(), name='events'),
    path('mechevents', MechanicEventsList.as_view(), name='mevents'),
    path('events', ManagerEventList.as_view(), name='mana-events'),
    path('event/create', EventCreate.as_view(), name='event-create'),
    path('event/create/<int:pk>', EventCreateII.as_view(), name='event-create2'),
    
    path('event/update/<int:pk>', EventUpdate.as_view(), name='event-update'),
    path('event/delete/<int:pk>', EventDelete.as_view(), name='event-delete'),
    path('event/raport/<int:pk>', MechanicEventUpdate.as_view(), name='event-raport')
]
