from django.shortcuts import render, redirect, get_object_or_404
from .models import Patient, Doctor, Appointment
from .forms import PatientForm, DoctorForm, AppointmentForm

def index(request):
    return render(request, 'index.html',{'section':'home'})


def patients(request):
    patients = Patient.objects.all()
    return render(request, 'patients.html',{'patients': patients,'section':'patients'})

def patient_create(request):
    form = PatientForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('patients')
    return render(request, 'patient_form.html', {'form': form})

def patient_update(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    form = PatientForm(request.POST or None, instance=patient)
    if form.is_valid():
        form.save()
        return redirect('patients')
    return render(request, 'patient_form.html', {'form': form})

def patient_delete(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        patient.delete()
        return redirect('patients')
    return render(request, 'patient_confirm_delete.html', {'patient': patient})


# ===================== DOCTORS =====================

def doctors(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctors.html',{'doctors': doctors,'section':'doctors'})

def doctor_create(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('doctors')
    else:
        form = DoctorForm()
    return render(request, 'doctor_form.html', {'form': form})

def doctor_update(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('doctors')
    else:
        form = DoctorForm(instance=doctor)
    return render(request, 'doctor_form.html', {'form': form})

def doctor_delete(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        doctor.delete()
        return redirect('doctors')
    return render(request, 'doctor_confirm_delete.html', {'doctor': doctor})

# ===================== APPOINTMENTS =====================

def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'appointment_list.html', {'appointments': appointments,'section':'appointments'})

def appointment_create(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment_list')
    else:
        form = AppointmentForm()
    return render(request, 'appointment_form.html', {'form': form})

def appointment_update(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('appointment_list')
    else:
        form = AppointmentForm(instance=appointment)
    return render(request, 'appointment_form.html', {'form': form})

def appointment_delete(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    if request.method == 'POST':
        appointment.delete()
        return redirect('appointment_list')
    return render(request, 'appointment_confirm_delete.html', {'appointment': appointment})
