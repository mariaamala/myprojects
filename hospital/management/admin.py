from django.contrib import admin
from .models import Doctor,Patient, Appointment  # Assuming you have both models

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialty','phone')

class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'gender','treatment','phone')

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'patient', 'date','time')
 # Adjust fields as per your model

admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Patient, PatientAdmin)
admin.site.register(Appointment, AppointmentAdmin)
