from enum import unique
from django.core import validators
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
import uuid

# Create your models here.

class Profile(models.Model):
    PHYSICAL_ACTIVITY_LEVEL = (
        ('1.2', 'Baja'),
        ('1.375', 'Ligera'),
        ('1.55', 'Moderada'),
        ('1.725', 'Intensa'),
    )
    SEX_TYPE = (
        ('m', 'Male'),
        ('f', 'Female'),
    )

    username = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    born_date = models.DateField(null=True, blank=True)
    height = models.IntegerField(
        validators = [
            MaxValueValidator(240), 
            MinValueValidator(100)
            ],
            null=True, 
            blank=True
        )
    sex = models.CharField(max_length=10, choices=SEX_TYPE,null=True, blank=True)
    weight = models.IntegerField(null=True, blank=True)
    physical_activity = models.CharField(max_length=5, choices=PHYSICAL_ACTIVITY_LEVEL,null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self) -> str:
        return self.name

class NutricionalInfo(models.Model):
    WEIGHTS = (
        ('1', 'Low weight'),
        ('2', 'Normal weight'),
        ('3', 'Overweight'),
        ('4', 'Obesity')
    )
    user = models.OneToOneField(Profile, on_delete=models.CASCADE)
    imc = models.IntegerField(null=True, blank=True)
    calories_day = models.IntegerField(null=True, blank=True)
    weight_status = models.CharField(max_length=20, choices=WEIGHTS, blank=True, null=True)
    meals_cant = models.IntegerField(validators=[MaxValueValidator(10)], null=True, blank=True)

    @property
    def calculateIMC(self):
        height = self.user.height / 100
        weight = self.user.weight
        self.imc = weight / (height**2)
        if self.imc < 18.5:
            self.weight_status = '1'
        elif self.imc >= 18.5 and self.imc < 24.9:
            self.weight_status = '2'
        elif self.imc >= 25.0 and self.imc < 29.9:
            self.weight_status = '3'
        else:
            self.weight_status = '4' 
        self.save()
    
    def calculateCalories(self):
        height = self.user.height
        weight = self.user.weight
        age = self.user.born_date
        sex = self.user.sex
        physical_activity = self.user.physical_activity

        if sex == 'm':
            self.calories_day = (66 + (13.7*weight) + (5*height) - (6.5*age)) * physical_activity
        elif sex == 'f':
            self.calories_day = ((10*weight) + (6.5*height) - (5*age) - 161) * physical_activity
        else:
            return 'Fill your biological sex'
        
        self.save()

    def __str__(self) -> str:
        return str(self.user)
