from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from .models import *
# from .forms import CustomerForm

class CustomLoginView(auth_views.LoginView):
    template_name = 'login/login.html'

class CustomLogoutView(auth_views.LogoutView):
    template_name = 'login/logout.html'

class CustomerView(DetailView):
    template_name = 'customer.html'
    model = Customer
    context_object_name = 'customer'

# class CustomerSignUp(CreateView):
#     template_name = 'signup.html'
#     success_url = reverse_lazy('login')
#     form_class = CustomerForm
    