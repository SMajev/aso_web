from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView, FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *
from .forms import *
from accounts.models import *
from django.urls import reverse_lazy
from datetime import timedelta  
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
        form.instance.customer = self.request.user.customer
        event = form.save()
        for service in form.cleaned_data.get('services'):
            event.ttd += service.time
        return super().form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse_lazy('event-create2', kwargs={'pk': self.object.pk})


class EventCreateII(UpdateView):
    template_name = 'event_create.html'
    form_class = EventFormII
    model = Event
    success_url = reverse_lazy('index')

    def datespan(self):
        today = datetime.datetime.today()
        delta1 = datetime.timedelta(days=14)
        delta2 = datetime.timedelta(days=1)
        later = today + delta1
        current_day = today
        while current_day < later:
            if current_day.weekday() < 5:
                yield current_day
                current_day += delta2
            else:
                current_day += delta2

    def datetime_dejavu_controler(self, date, datetime_list):
        if date not in datetime_list:
            return True

    def date_converter(self, event):
        if type(event) != str:
            event_start_pre = event.date.strftime('%Y-%m-%d %H:%M:%S')
            event_end_pre = event.enddate.strftime('%Y-%m-%d %H:%M:%S')
            event_start = datetime.datetime.strptime(event_start_pre,'%Y-%m-%d %H:%M:%S')
            event_end = datetime.datetime.strptime(event_end_pre, '%Y-%m-%d %H:%M:%S')
            return (event_start, event_end)
        else:
            print(type(event))
            datetime_object = datetime.datetime.strptime(event,'%Y-%m-%d %H:%M:%S')
            return datetime_object

    def check_availability(self, new_event):
        stations = Station.objects.all()
        avail_list = []
        aso_open = 6
        aso_closed = 18
        hours_of_work = 10
    
        for day in self.datespan():


            for station in stations:
                start_time = day.replace(day=day.day,hour=aso_open, minute=0, second=0, microsecond=0)
                end_time = start_time + datetime.timedelta(hours=hours_of_work)
                current_time = start_time
                one_hour = datetime.timedelta(hours=1)
                events = Event.objects.filter(station=station, date=current_time)                
                time_of_work = end_time - start_time
                free_hours = 0
                spread = []
                new_event_ttd = new_event.ttd
                while current_time != end_time:
                    spread.append(current_time)
                    current_time += one_hour

                for now_hour in spread:
                    print(now_hour)
                    if 0  < len(events):
                        for event in events:
                            event_start, event_end = self.date_converter(event)
                            if now_hour == event_end:
                                if self.datetime_dejavu_controler(event_end, avail_list):
                                    avail_list.append((now_hour, now_hour))
                    elif free_hours == new_event_ttd:
                        open_hour = now_hour + datetime.timedelta(hours=new_event_ttd)
                        if self.datetime_dejavu_controler(event_end, avail_list):
                                    avail_list.append((open_hour, open_hour))   
                    else:
                        free_hours += 1
                        print(free_hours)

        print(avail_list)


                    
                    # 
                    # for event in schedule:
                    #     if event:
                    #         end_event = event.enddate
                    #         if new_event_ttd <= (start_time - end_time):
                    #             avail_list.append((end_event, end_event))
                    #     elif None:
                    #         free_hours += 1
                    #         if free_hours == new_event_ttd:
                    #             avail_list.append((end_time, end_time))


                            # if datetime.timedelta(hours=new_event_ttd) <= (start_time - end_time):
                                
                            #     if self.datetime_dejavu_controler(end_time, avail_list):
                            #         avail_list.append((end_time, end_time))
                            #         dattee = day.replace(hour=datetime.timedelta(hours=(clock + 1)))
                            #         hours -= new_event_ttd



                    


        return avail_list


    def get_form(self):
        form = super().get_form() 
        # avail_list, station = 
        form.fields['date'].choices = self.check_availability(self.get_object())
        return form

    def form_valid(self, form):
        form.instance.customer = self.request.user.customer   
        event = form.save()
        start_date = form.cleaned_data.get('date')
        event.enddate = self.date_converter(start_date) + timedelta(hours=event.ttd)
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