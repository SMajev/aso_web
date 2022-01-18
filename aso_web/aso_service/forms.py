from django import forms
from .models import Event

class DateInput(forms.DateInput):
    input_type = 'date'


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['date', 'car_id', 'car_model', 'services']
        widgets = {
            'date': DateInput(),
        }




