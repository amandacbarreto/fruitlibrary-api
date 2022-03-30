from django.db import models

# Create your models here.
class Region(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name

class Fruit(models.Model):
    name = models.CharField(max_length=80)
    region = models.ForeignKey(Region, on_delete=models.PROTECT, related_name="fruits")

    def __str__(self):
        return self.name