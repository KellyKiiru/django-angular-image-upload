from django.db import models

class Image(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=50)
    image = models.BinaryField()

    def __str__(self):
        return self.name