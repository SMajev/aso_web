from django import forms
from .models import Event, EventBooker, Station
from accounts.models import Mechanic
import datetime
from django.db.transaction import atomic

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['car_id', 'car_model', 'services']


class EventFormII(forms.ModelForm):
    date_start = forms.DateField(widget=forms.DateInput(format=('%d-%m-%Y')))
    date_end = forms.DateField(widget=forms.DateInput(format=('%d-%m-%Y')))
    time_start = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
    time_end = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))

class ManagerEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'

class MechanicRaportForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['raport']

    raport = forms.CharField(widget=forms.Textarea(attrs={'rows':5, 'cols':30, 'style':'resize:none'}), required=False, )
