from django.urls import path
from .views import (
    CustomerView, CustomLoginView, CustomLogoutView,
        CustomerSignUp, MechanicSignUp, MechanicView
)


urlpatterns = [
    path('profile/<int:pk>', CustomerView.as_view(), name='profile'),
    path('mprofile/<int:pk>', MechanicView.as_view(), name='profile'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('sign-up/', CustomerSignUp.as_view(), name='signup'),
    path('msign-up', MechanicSignUp.as_view(), name='msignup')
]
