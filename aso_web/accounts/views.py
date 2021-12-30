from django.views.generic import DetailView
from django.contrib.auth import views as auth_views
from .models import *

class CustomLoginView(auth_views.LoginView):
    template_name = 'login/login.html'

class CustomLogoutView(auth_views.LogoutView):
    template_name = 'login/logout.html'

class CustomerView(DetailView):
    template_name = 'customer.html'
    model = Customer
    context_object_name = 'customer'