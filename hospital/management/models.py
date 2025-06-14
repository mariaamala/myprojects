from django.db import models

# class Doctor(models.Model):
#     name = models.CharField(max_length=100)
#     specialty = models.CharField(max_length=100,default='')
#     phone = models.CharField(max_length=15,default='0000000000')

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    image_url = models.CharField(max_length=2085, null=True, blank=True)

    def __str__(self):
        return self.name


class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    treatment = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)


class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
