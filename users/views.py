from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from .form import UserForm
# Create your views here.

def home(request):
    error = ''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            
            if user.is_doctor:
                return redirect('doctor')
            
            elif user.is_infirmiere:
                return redirect('infirmiere')
            
            else:
                return redirect('patient')
        else:
            error = 'password or username wrong'
            
    return render(request, 'login.html', {'error':error})


def register(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'register.html', {'form':form})


def doctor(request):
    return render(request, 'doctor.html')

def infirmiere(request):
    return render(request, 'infirmiere.html')

def patient(request):
    return render(request, 'patient.html')