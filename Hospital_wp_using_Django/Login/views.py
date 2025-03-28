from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render
from .models import Department, Doctor, Appointment


# EMPLOYEE LOGIN
def employee_login(request):
    
    if request.method == "POST":
        email = request.POST.get('email').lower()
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(email = email)
        except:
            messages.error(request, "Username does not exist")
    return render(request, 'base/employee_login.html')


def employee_logout(request):
    return redirect('base/home.html')


def register_EmpFrm(request):
    
    if request.method == "POST":
        form = MyUserCreationForm(request.POST)
        if request.method == "POST":
            form = MyUserCreationForm(request.POST)
            if form.is_valid():
                user = form.save(commit = False)
                user.username = user.username.lower()
                user.save()
                login(request, user)
                return redirect('home')
    return redirect('base/home.html')


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def departments(request):
    departments = Department.objects.all()
    return render(request, 'departments.html', {'departments': departments})

def doctors(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctors.html', {'doctors': doctors})

def patient_portal(request):
    return render(request, 'patient_portal.html')

def appointments(request):
    appointments = Appointment.objects.filter(patient=request.user)
    return render(request, 'appointments.html', {'appointments': appointments})

def contact(request):
    return render(request, 'contact.html')
