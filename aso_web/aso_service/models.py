from django.db import models
from django.contrib.auth.models import User
from accounts.models import Customer, Mechanic
import datetime as dt


# def datespan():
#     today = dt.datetime.today()
#     delta1 = dt.timedelta(days=5)
#     delta2 = dt.timedelta(days=1)
#     later = today + delta1
#     current_day = today
#     while current_day < later:
#         if current_day.weekday() < 5:
#             yield current_day
#             current_day += delta2
#         else:
#             current_day += delta2

# def spread_maker(current_time, end_time, one_hour):
#         spread = []
#         while current_time != end_time:
#             spread.append(current_time)
#             current_time += one_hour
#         return spread



class Station(models.Model):
    name = models.CharField(max_length=20, default='Position')
    start_time = models.TimeField(default=dt.time(hour=6, minute=0, second=0, microsecond=0))
    now_time = models.TimeField(default=start_time)
    hour_time = models.TimeField(default=dt.timedelta(hours=1))
    end_time = models.TimeField(default=dt.time(hour=18, minute=0, second=0, microsecond=0))
    timeline = models.JSONField(default=None)
    # timeline_daily = spread_maker(now_time, end_time, hour_time)
    # timeline_week = datespan()
    

    def __str__(self):
        return f'{self.name}{self.pk}'
    

class Service(models.Model):
    title = models.CharField(max_length=128)
    describe = models.CharField(max_length=256)
    time = models.IntegerField()
    price = models.IntegerField()
    def __str__(self):
        return f"{self.title}, Time: {self.time}h, Price:{self.price}$"
    
    
class EventBooker(models.Model):
    station = models.ForeignKey(Station, on_delete=models.DO_NOTHING, null=True, blank=True)
    date_start = models.DateField(null=True, blank=True)
    date_end = models.DateTimeField(null=True, blank=True)
    time_start = models.TimeField(null=True, blank=True)
    time_end = models.TimeField(null=True, blank=True)
    duration_time = models.IntegerField(default=0)
    

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
    event_booker = models.ForeignKey(EventBooker, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    mechanic = models.ForeignKey(Mechanic, on_delete=models.DO_NOTHING, null=True, blank=True)
    car_id = models.CharField(max_length=15)
    car_model = models.CharField(max_length=15, choices=CAR_MODEL_CHOICE, default=CAR_MODEL_CHOICE[0][0])
    services = models.ManyToManyField(Service)
    raport = models.CharField(max_length=500, blank=True)
    created = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICE, default=STATUS_CHOICE[0][0])
    
    def __str__(self):
        return f'ID: {str(self.pk)}, Customer: {self.customer}, Mechanic: {self.mechanic}'


