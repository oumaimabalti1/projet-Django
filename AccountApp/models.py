from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator, RegexValidator


class User(AbstractUser):
    pass



class Speciality(models.Model):
    name = models.CharField(max_length=100)


class Doctor(User):
    licence_number = models.CharField(max_length=6, unique=True)
    phone_number = models.CharField(max_length=8, validators = [RegexValidator(r"^\d{8}$", message="Le téléphone doit contenir 8 chiffres.")])
    specialities = models.ManyToManyField(Speciality, related_name='doctors')

class Patient(User):
    national_id = models.CharField(max_length=8, unique=True)
    phone = models.CharField(max_length=8, validators = [RegexValidator(r"^\d{8}$", message="Le téléphone doit contenir 8 chiffres.")])
    birth_date = models.DateField()