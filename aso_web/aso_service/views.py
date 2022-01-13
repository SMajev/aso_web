from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, FormView
from .models import *
from .forms import *
from accounts.models import *
from django.urls import reverse_lazy


class Index(TemplateView):
    template_name = 'index.html'

class AboutView(TemplateView):
    template_name = 'about.html'


class Services(ListView):
    template_name = 'services.html'
    model = Service
    context_object_name = 'services'


class EventCreateView(FormView):
    template_name = 'event_create.html'
    form_class = EventForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.customer = self.request.user.customer
        form.save()
        return super().form_valid(form)
