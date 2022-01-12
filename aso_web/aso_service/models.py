from django.db import models
from django.contrib.auth.models import User
from accounts.models import Customer, Mechanic


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
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateField()
    car_id = models.CharField(max_length=15)
    car_model = models.CharField(max_length=15)
    services = models.ManyToManyField(Service)
    raport = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICE, default=STATUS_CHOICE[0][0])
    
    def __str__(self):
        return str(self.pk)
    