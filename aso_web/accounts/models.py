from django.db import models
from django.contrib.auth.models import User
from aso_service.models import Service, Event

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default=None)
    surname = models.CharField(max_length=100, default=None)
    email = models.EmailField(default=None)
    pesel = models.CharField(max_length=10, default=None)

    def delete(self, using=None, keep_parents=False):
        self.user.delete()
        return super().delete(using, keep_parents)

    def __str__(self):
        return self.user.username

class Customer(Profile):
    events = models.ManyToManyField(Event, blank=True)

    def delete(self, using=None, keep_parents=False):
        self.user.delete()
        return super().delete(using, keep_parents)

    def __str__(self):
        return self.user.username

class Mechanic(Profile):
    completed_events = models.ManyToManyField(Event, blank=True)

    def delete(self, using=None, keep_parents=False):
        self.user.delete()
        return super().delete(using, keep_parents)

    def __str__(self):
        return self.user.username

