from django.db import models

# Create your models here.
class User(AbstractUser):
    pass

class Specialist(models.Model):
    name = models.CharField(max_length=100)

class Doctor(User):
    license_number = models.CharField(max_length=6, unique=True)
    phone = models.CharField(max_length=8)

class Patient(User):
    national_id = models.CharField(max_length=8, unique=True)
    phone = models.CharField(max_length=8)
    birth_date = models.DateField()