from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import *
from accounts.models import *


class Index(TemplateView):
    template_name = 'index.html'

class Services(ListView):
    template_name = 'services.html'
    model = Service
    context_object_name = 'services'

class CustomerView(DetailView):
    template_name = 'customer.html'
    model = Customer
    context_object_name = 'customer'
