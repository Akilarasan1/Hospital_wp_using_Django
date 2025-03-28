from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

class Employee(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)

class Patient(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=15)

class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.name

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100)
    availability = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Appointment(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    reason = models.TextField()
    
    def __str__(self):
        return f"Appointment for {self.patient.username} with {self.doctor.name} on {self.date} at {self.time}"


##after create models, python manage.py makemigrations and python manage.py migrate