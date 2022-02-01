from django.db import models

# Create your models here.

class Doctor(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    

class Patient(models.Model):
    patient_number = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    doctor = models.ManyToManyField(Doctor, blank=True,null=True, related_name="doctor")
    sectionTelegramId = models.CharField(max_length=255, blank=True, null=True)

class Report(models.Model):
    # heartrate = models.IntegerField()
    alarm = models.BooleanField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    create_date = models.DateField(auto_now_add=True)