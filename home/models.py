from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=125)
    email=models.CharField(max_length=125)
    phone=models.CharField(max_length=12)
    desc=models.CharField(max_length=250)
    date=models.DateField()

    def __str__(self):
        return self.name

