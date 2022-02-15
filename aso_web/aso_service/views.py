from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView, FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *
from .forms import *
from accounts.models import *
from django.urls import reverse_lazy
import datetime as dt
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.utils import timezone
from django.utils.timezone import make_aware

# ------------------------ General ------------------------

class Index(TemplateView):
    template_name = 'index.html'

class AboutView(TemplateView):
    template_name = 'about.html'


# ------------------------ Service ----------------------------

class Services(ListView):
    template_name = 'services.html'
    model = Service
    context_object_name = 'services'


# ------------------------ Event General ------------------------

class EventDetail(DetailView):
    template_name = 'event_detail.html'
    model = Event
    context_object_name = 'event'

class EventCreate(CreateView):
    template_name = 'event_create.html'
    form_class = EventForm
    success_url = reverse_lazy('event-create2')

    def form_valid(self, form):
        self.event = form.save(commit=False)   
        self.event.customer = self.request.user.customer
        self.event.event_booker = EventBooker.objects.create()
        self.event.save()
        for service in self.event.services.all():
            event.duration += service.time

        self.event.save()
        return super().form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse_lazy('event-create2', kwargs={'pk': self.object.pk})


class EventCreateII(UpdateView):
    template_name = 'event_create.html'
    form_class = EventFormII
    model = Event
    success_url = reverse_lazy('index')

    def datespan(self):
        today = dt.datetime.today()
        delta1 = dt.timedelta(days=5)
        delta2 = dt.timedelta(days=1)
        later = today + delta1
        current_day = today
        while current_day < later:
            if current_day.weekday() < 5:
                yield current_day
                current_day += delta2
            else:
                current_day += delta2

    def datetime_dejavu_controler(self, date, datetime_list):
        if date in datetime_list:
            return False

    def final_tuple_append(self, data, my_list):
        print((data, data))
        my_list.append((data, data))

    def spread_maker(self, current_time, end_time, one_hour):
        spread = []
        while current_time != end_time:
            spread.append(current_time)
            current_time += one_hour
        return spread


    def date_converter(self, event):
        print(event)
        if type(event) != str:
            event_start_pre = event.date.strftime('%d-%m-%Y %H:%M:%S')
            event_end_pre = event.enddate.strftime('%d-%m-%Y %H:%M:%S')
            event_start = dt.datetime.strptime(event_start_pre,'%d-%m-%Y %H:%M:%S')
            event_end = dt.datetime.strptime(event_end_pre, '%d-%m-%Y %H:%M:%S')
            return (event_start, event_end)
        # else:
        #     print(type(event))
        #     datetime_object = datetime.datetime.strptime(event,'%d-%m-%Y %H:%M:%S')
        #     return datetime_object

    # def Controler_I(self):

    def check_availability(self, new_event):
        stations = EventBooker.station.objects.all()
        avail_list = []
        aso_open = 6
        hours_of_work = 10
    
        for day in self.datespan():
            for station in stations:
                start_time = day.replace(day=day.day,hour=aso_open, minute=0, second=0, microsecond=0)
                current_time = start_time
                one_hour = dt.timedelta(hours=1)
                end_time = start_time + dt.timedelta(hours=hours_of_work)
                time_of_work = end_time - start_time  
                duration = dt.timedelta(hours=new_event.ttd)
                spread = self.spread_maker(current_time, end_time, one_hour)
                loop_on = True
                free_hours = 0
                events = Event.objects.filter(station=station)
                print('\n\n\n\n\n\n')
                print(events)
                for now_hour in spread:
                    if (len(events) > 1) and ((now_hour + duration) <= end_time):
                        for i in range(len(events)):
                            for j in range(i+1, len(events)-1):
                                event_start, event_end = self.date_converter(event[i])
                                print(event_start, event_end)
                                if (duration <= (event_start - start_time)) or (duration <= (next_event - event_start)):
                                    if self.datetime_dejavu_controler(now_hour, spread):
                                        self.final_tuple_append(now_hour, avail_list)
                                        



        return avail_list


    def get_form(self):
        form = super().get_form() 
        avail_list = self.check_availability(self.get_object())
        form.fields['date'].choices = avail_list
        
        return form

    def form_valid(self, form):
        form.instance.customer = self.request.user.customer   
        event = form.save()
        start_date = form.cleaned_data.get('date')
        event.enddate = self.date_converter(start_date) + timedelta(hours=event.ttd)
        # position = event.cleaned_data.get('size')
        # form.save()
        print(event)
        return super().form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse_lazy('index')


# ------------------------ Event Customer ------------------------

class CustomerEventsList(ListView):
    template_name = 'customer_events.html'
    model = Event
    context_object_name = 'events'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['events'] = Event.objects.filter(customer=self.request.user.customer)
        return context

# ------------------------ Event Mechanic ------------------------

class MechanicEventsList(ListView):
    template_name = 'mechanic_events.html'
    model = Event
    context_object_name = 'events'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['events'] = Event.objects.filter(mechanic=self.request.user.mechanic)
        return context
    

class MechanicEventUpdate(UpdateView):
    template_name = 'event_create.html'
    form_class = MechanicRaportForm
    model = Event
    success_url = reverse_lazy('index')


# ------------------------ Event Manager ------------------------

class ManagerEventList(PermissionRequiredMixin, ListView):
    template_name = 'events.html'
    model = Event
    context_object_name = 'events'
    permission_required = 'aso_service.update_event'

class EventUpdate(PermissionRequiredMixin, UpdateView):
    template_name = 'event_create.html'
    form_class = ManagerEventForm
    model = Event
    success_url = reverse_lazy('index')
    permission_required = 'aso_service.update_event'

class EventDelete(PermissionRequiredMixin, DeleteView):
    template_name = 'event_delete.html'
    model = Event
    success_url = reverse_lazy('events')
    permission_required = 'aso_service.delete_event'





    # def date_converter(self, string, time):
    #     ddate =  datetime.datetime.strptime(string, '%Y-%m-%d %H:%M:%S')
    #     book_day_time = datetime.datetime.combine(ddate, time)
    #     return (book_day_time, book_day_time)