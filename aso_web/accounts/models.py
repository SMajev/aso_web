from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def delete(self, using=None, keep_parents=False):
        self.user.delete()
        return super().delete(using, keep_parents)

    def __str__(self):
        return self.user.username
    

class Mechanic(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def delete(self, using=None, keep_parents=False):
        self.user.delete()
        return super().delete(using, keep_parents)

    def __str__(self):
        return self.user.username
    

class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def delete(self, using=None, keep_parents=False):
        self.user.delete()
        return super().delete(using, keep_parents)

    def __str__(self):
        return self.user.username

class Manager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def delete(self, using=None, keep_parents=False):
        self.user.delete()
        return super().delete(uising, keep_parents)

    def __str__(self):
        return self.user.username
    

