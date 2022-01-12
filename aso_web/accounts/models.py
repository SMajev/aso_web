from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pesel = models.CharField(max_length=10, default=None)

    def delete(self, using=None, keep_parents=False):
        self.user.delete()
        return super().delete(using, keep_parents)

    def __str__(self):
        return self.user.username

class Customer(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)

    def delete(self, using=None, keep_parents=False):
        self.profile.delete()
        return super().delete(using, keep_parents)


class Mechanic(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)

    def delete(self, using=None, keep_parents=False):
        self.profile.delete()
        return super().delete(using, keep_parents)

    def __str__(self):
        return self.profile.username

