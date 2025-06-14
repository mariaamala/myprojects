from django.urls import path
from . import views

urlpatterns = [
     path('', views.index, name='index'),
     path('doctors/', views.doctors, name='doctors'),
    path('patients/', views.patients, name='patients'),

    # Patients
    path('patients/', views.patients, name='patients'),
    path('patients/add/', views.patient_create, name='patient_create'),
    path('patients/edit/<int:pk>/', views.patient_update, name='patient_update'),
    path('patients/delete/<int:pk>/', views.patient_delete, name='patient_delete'),

    # Doctors
    path('doctors/', views.doctors, name='doctors'),
    path('doctors/add/', views.doctor_create, name='doctor_create'),
    path('doctors/edit/<int:pk>/', views.doctor_update, name='doctor_update'),
    path('doctors/delete/<int:pk>/', views.doctor_delete, name='doctor_delete'),

    # Appointments
    path('appointments/', views.appointment_list, name='appointment_list'),
    path('appointments/add/', views.appointment_create, name='appointment_create'),
    path('appointments/edit/<int:pk>/', views.appointment_update, name='appointment_update'),
    path('appointments/delete/<int:pk>/', views.appointment_delete, name='appointment_delete'),
]
