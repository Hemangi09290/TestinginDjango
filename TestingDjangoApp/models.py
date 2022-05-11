from django.db import models

# Create your models here.
class Animals(models.Model):
    name = models.CharField(max_length=255)
    sound = models.CharField(max_length=255)
    

    def __str__(self):
        return f'{self.name}, {self.sound}'

    # we can define model method like this
    def animal_sounds(self):
        return f'{self.name} says {self.sound}'
    