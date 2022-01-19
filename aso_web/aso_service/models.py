from django.db import models
from django.contrib.auth.models import User
from accounts.models import Customer, Mechanic

class Station(models.Model):
    name = models.CharField(max_length=20, default='Position')
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return self.name
    

class Service(models.Model):
    title = models.CharField(max_length=128)
    describe = models.CharField(max_length=256)
    time = models.IntegerField()
    price = models.IntegerField()
    def __str__(self):
        return self.title
    
     
class Event(models.Model):
    STATUS_CHOICE = (
        ('Draft', 'Draft'), 
        ('In Progress', 'In Progress'),
        ('Complete', 'Complete')
    )
    CAR_MODEL_CHOICE = (
        ('X', 'Unknown'), ('A1', 'A1'), ('A2', 'A2'),
        ('A3','A3'), ('A4','A4'), ('A5', 'A5'), ('A6','A6'), 
        ('A7','A7'), ('80', '80'), ('90', '90'), ('100', '100'),
        ('200', '200')
    )
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    mechanic = models.ForeignKey(Mechanic, on_delete=models.DO_NOTHING, null=True, blank=True)
    station = models.ForeignKey(Station, on_delete=models.DO_NOTHING, null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)
    ttd = models.IntegerField(default=0)
    enddate = models.DateTimeField(null=True, blank=True)
    car_id = models.CharField(max_length=15)
    car_model = models.CharField(max_length=15, choices=CAR_MODEL_CHOICE, default=CAR_MODEL_CHOICE[0][0])
    services = models.ManyToManyField(Service)
    raport = models.CharField(max_length=500, blank=True)
    created = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICE, default=STATUS_CHOICE[0][0])
    
    def __str__(self):
        return f'ID: {str(self.pk)}, Customer: {self.customer}, Mechanic: {self.mechanic}, Station: {self.station}'

    