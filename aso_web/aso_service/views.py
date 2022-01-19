from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView, FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *
from .forms import *
from accounts.models import *
from django.urls import reverse_lazy
from datetime import timedelta  
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin



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

    def check_availability(self, new_event):
        stations = Station.objects.all()
        avail_list = []
        hours = [(datetime.time(i).strftime('%I')) for i in range(6, 18)]
        for station in stations:
            events = Event.objects.filter(station=station)
            if len(events) > 0:
                for i in range(len(events)):
                    for j in range(i+1, len(events)):
                        print(j)
                        if datetime.timedelta(hours=new_event.ttd) < (events[j].date - events[i].enddate):
                            avail_list.append(events[i].enddate)

                        else:
                            continue       
            else:
                avail_list.append(station.start_time)

        print(f'Dostępny termin: {avail_list}')
        return avail_list

    def get_initial(self):
        initial = super(EventCreateII, self).get_initial()
        form = self.form
        # initial['date'] = self.check_availability(self.object)
        form['date'].choices = self.check_availability(self.object)
        return initial


    def form_valid(self, form):   
        start_date = form.cleaned_data.get('date')
        event = form.save()
        event.enddate = start_date + timedelta(hours=event.ttd)
        form.save()
        return super().form_valid(form)


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




