from django import forms
from .models import Event
from accounts.models import Mechanic
import datetime


TODAY = datetime.date.today()
MONTHS = ['zero','January','February','March','April','May','June','July','August','September','October','November','December']
CURRENT_MONTH = MONTHS[TODAY.month]

# class DateInput(forms.DateInput):
#     input_type = 'date'




class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['car_id', 'car_model', 'services']

class EventFormII(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['date']

    # date = forms.MultipleChoiceField()

    # def __init__(self, *args, **kwargs):
    #     super(EventFormII, self).__init__(*args, **kwargs)
    #     self.fields["date"].initial = 
        
class ManagerEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'

class MechanicRaportForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['raport', 'status']

    raport = forms.CharField(widget=forms.Textarea(attrs={'rows':5, 'cols':30, 'style':'resize:none'}), required=False, )
