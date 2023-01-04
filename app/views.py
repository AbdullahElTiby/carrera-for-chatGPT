from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import login
from django.contrib import messages
from . models import Customuser
# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def batteryserivce(request):
    return render(request, 'battery-serivce.html')

def carwash(request):
    return render(request, 'car-wash.html')

def contact(request):
    return render(request, 'contact.html')

def enginoilservice(request):
    return render(request, 'engin-oil-service.html')

def fueldelivery(request):
    return render(request, 'fuel-delivery.html')

def gallery1(request):
    return render(request, 'gallery-1.html')

def loginpage(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        phonenumber = request.POST['phonenumber']
        # adress = request.POST['adress']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if password == password2:
            if Customuser.objects.filter(email=email).exists():
                messages.info(request, 'Email Already used')
                return redirect('loginpage')
            elif Customuser.objects.filter(username=username).exists():
                messages.info(request, 'Username Already used')
                return redirect('loginpage')
            elif Customuser.objects.filter(phonenumber=phonenumber).exists():
                messages.info(request, 'Your phone number is Already used')
                return redirect('loginpage')            
            
            else:
                user = Customuser.objects.create_user(username=username, email=email, password=password)
                user.save();
                return redirect('signin')
        else:
            messages.info(request, 'Password is not the same')
            return redirect('loginpage')
    return render(request, 'loginpage.html')



def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'credentials invalid')
            return redirect('signin')
            
            
    return render(request, 'signin.html')

def reservationform(request):
    return render(request, 'reservation-form.html')

def service1(request):
    return render(request, 'service-1.html')

def towtruckservice(request):
    return render(request, 'tow-truck-service.html')

def tryeservice(request):
    return render(request, 'trye-service.html')

def visapayment(request):
    return render(request, 'visa-payment.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def profilepage(request):
    return render(request, 'profilepage.html')

def index2(request):
    return render(request, 'index2.html')
