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
        ('X', 'In Progress'), ('V', 'Complete')
    )
    CAR_MODEL_CHOICE = (
        ('X', 'Unknown'), ('A1', 'A1'), ('A2', 'A2'),
        ('A3','A3'), ('A4','A4'), ('A5', 'A5'), ('A6','A6'), 
        ('A7','A7'), ('80', '80'), ('90', '90'), ('100', '100'),
        ('200', '200')
    )
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    mechanic = models.ForeignKey(Mechanic, on_delete=models.DO_NOTHING, null=True, blank=True)
    date = models.DateField()
    ttd = models.IntegerField(default=0)
    enddate = models.DateField(null=True, blank=True)
    car_id = models.CharField(max_length=15)
    car_model = models.CharField(max_length=15, choices=CAR_MODEL_CHOICE, default=CAR_MODEL_CHOICE[0][0])
    services = models.ManyToManyField(Service)
    raport = models.CharField(max_length=500, blank=True)
    created = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICE, default=STATUS_CHOICE[0][0])
    
    def __str__(self):
        return str(self.pk)
    