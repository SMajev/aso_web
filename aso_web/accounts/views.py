from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from .models import *
from .forms import CustomerRegistrationForm, MechanicRegistrationForm

# ------------------------ Customer ------------------------

class CustomLoginView(auth_views.LoginView):
    template_name = 'login/login.html'


class CustomLogoutView(auth_views.LogoutView):
    template_name = 'login/logout.html'


class CustomerView(DetailView):
    template_name = 'account/customer.html'
    model = User
    context_object_name = 'customer'


class CustomerSignUp(CreateView):
    template_name = 'login/signup.html'
    success_url = reverse_lazy('login')
    form_class = CustomerRegistrationForm



# ------------------------ Mechaqnic ------------------------

class MechanicView(DetailView):
    template_name = 'account/customer.html'
    model = Mechanic
    context_object_name = 'customer'


class MechanicSignUp(CreateView):
    template_name = 'login/signup.html'
    success_url = reverse_lazy('login')
    form_class = MechanicRegistrationForm
        

class AccountUpdate(UpdateView):
    template_name = 'login/signup.html'
    model = User
    success_url = reverse_lazy('login')
    form_class = MechanicRegistrationForm