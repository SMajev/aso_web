from django.urls import path
from .views import CustomerView, CustomLoginView, CustomLogoutView


urlpatterns = [
    path('profile/<int:pk>', CustomerView.as_view(), name='profile'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout')
]
