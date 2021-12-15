from django.db import models
from django.contrib.auth.models import User

class Service(models.Model):
    title = models.CharField(max_length=128)
    describe = models.CharField(max_length=256)
    time = models.IntegerField()
    price = models.IntegerField()

class Event(models.Model):
    date = models.DateField()
    services = models.ManyToManyField(Service)
    worker = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    raport = models.CharField(max_length=500, blank=True)
    created = models.DateTimeField(auto_now=True)