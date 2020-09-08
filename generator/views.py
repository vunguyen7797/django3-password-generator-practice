from django.shortcuts import render
from django.http import  HttpResponse
import random
# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def password(request):
    my_password = ''

    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    if request.GET.get('specialcharacter'):
        characters.extend('!@#$%^&*()_+')

    if request.GET.get('number'):
        characters.extend('0123456789')

    length = int(request.GET.get('length',12))

    for x in range(length):
        my_password += random.choice(characters)


    return render(request, 'generator/password.html', {'password': my_password})

def about(request):

    my_info = 'This Password Generator was created by VU NGUYEN'
    return render(request, 'generator/about.html',{'about':my_info})
