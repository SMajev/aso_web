from django.db import models
from django.contrib.auth.models import User


class Service(models.Model):
    title = models.CharField(max_length=128)
    describe = models.CharField(max_length=256)
    time = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return self.title
    
     
class Event(models.Model):
    STATUS_CHOICE = (
        ('V', 'In Progress'), ('X', 'Complete')
    )
    date = models.DateField()
    services = models.ManyToManyField(Service)
    raport = models.CharField(max_length=500, blank=True)
    created = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICE, default=STATUS_CHOICE[0][0])
    
    def __str__(self):
        return str(self.pk)
    