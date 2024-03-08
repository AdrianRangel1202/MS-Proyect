from django.db import models
from django.contrib.auth.hashers import make_password


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length = 100, unique= True)
    email = models.EmailField(max_length = 100)
    password = models.CharField(max_length = 100)
   
    def __str__(self):   
        return self.username