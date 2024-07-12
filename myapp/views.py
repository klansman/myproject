from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Services
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def index(request):
    service = Services.objects.all()
    return render(request, 'index.html', {'services': service})

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already registered')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already registered')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save();
                return redirect('login')
        else:
            messages.info(request, 'Passwords do not match')
            return redirect('register')
    else:        
        return render(request, 'register.html')