from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class room(models.Model):
    name = models.CharField(max_length=100)
    room_number = models.IntegerField()
    floor = models.IntegerField()
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='rooms/images/', blank=True)

    def __str__(self):
        return self.name


    
    