from django.db import models

class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    new_number = models.CharField(max_length=15)
    age = models.IntegerField()

    def __str__(self):
        return self.name
