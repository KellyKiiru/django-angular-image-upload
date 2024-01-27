from django.db import models

class Image(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField()

    def __str__(self):
        return self.name
    
class Specialist(models.Model):
    name = models.CharField(max_length=255)