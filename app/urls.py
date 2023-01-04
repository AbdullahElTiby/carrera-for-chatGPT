from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index, name='index'),
    path('about.html', views.about, name='about'),
    path('battery-serivce.html', views.batteryserivce, name='battery-serivce'),
    path('car-wash.html', views.carwash, name='car-wash'),
    path('contact.html', views.contact, name='contact'),
    path('engin-oil-service.html', views.enginoilservice, name='engin-oil-service'),
    path('fuel-delivery.html', views.fueldelivery, name='fuel-delivery'),
    path('gallery-1.html', views.gallery1, name='gallery-1'),
    path('reservation-form.html', views.reservationform, name='reservation-form'),
    path('service-1.html', views.service1, name='service-1'),
    path('tow-truck-service.html', views.towtruckservice, name='tow-truck-service'),
    path('trye-service.html', views.tryeservice, name='trye-service'),
    path('visa-payment.html', views.visapayment, name='visa-payment'),
    path('loginpage.html', views.loginpage, name='loginpage'),
    path('signin.html', views.signin, name='signin'),
    path('logout', views.logout, name='logout'),
    path('profilepage.html', views.profilepage, name='profilepage'),
]
