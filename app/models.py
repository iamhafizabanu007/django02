from django.db import models

# Create your models here.
class students(models.Model):
    email=models.EmailField(max_length=100)
    name=models.CharField(max_length=100)