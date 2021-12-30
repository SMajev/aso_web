from django.urls import path
from .views import CustomerView, CustomLoginView


urlpatterns = [
    path('panel/<int:pk>', CustomerView.as_view(), name='panel'),
    path('login/', CustomLoginView.as_view(), name='login')
]
