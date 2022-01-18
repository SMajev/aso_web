from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView, FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *
from .forms import *
from accounts.models import *
from django.urls import reverse_lazy
from datetime import timedelta  
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
    success_url = reverse_lazy('index')

    def form_valid(self, form):   
        form.instance.customer = self.request.user.customer
        start_date = form.cleaned_data.get('date')
        event = form.save()
        for service in form.cleaned_data.get('services'):
            event.ttd += service.time
        
        event.enddate = start_date + timedelta(days=event.ttd)
        form.save()
        return super().form_valid(form)


class EventUpdate(UpdateView):
    template_name = 'event_create.html'
    form_class = EventForm
    success_url = reverse_lazy('index')


# ------------------------ Event Customer ------------------------

class CustomerEventsList(ListView):
    template_name = 'customer_events.html'
    model = Event
    context_object_name = 'events'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['events'] = Event.objects.filter(customer=self.request.user.customer)
        return context

# ------------------------ Event Staff ------------------------

class MechanicEventsList(ListView):
    template_name = 'mechanic_events.html'
    model = Event
    context_object_name = 'events'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['events'] = Event.objects.filter(mechanic=self.request.user.mechanic)
        return context







