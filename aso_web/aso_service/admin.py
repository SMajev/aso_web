from django.contrib import admin
from .models import *

admin.site.register(Station)
admin.site.register(Service)
admin.site.register(EventBooker)
admin.site.register(Event)

