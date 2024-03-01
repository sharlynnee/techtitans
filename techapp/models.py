from django.db import models

# Create your models here.
class Users(models.Model):
    fullname = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.username

