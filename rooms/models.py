from django.db import models

# Create your models here.

class rooms(models.Model):
    name = models.CharField(max_length=100)
    room_number = models.IntegerField()
    floor = models.IntegerField()
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='rooms/')
    
    