from django.shortcuts import render
from django.http import HttpResponse
#Now, in order to generate a random password
import random
# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    if request.GET.get('special'):
        characters.extend(list('!@&#$*+()<>'))

    #default passwort situation
    length = int(request.GET.get('lenght',12))
    thepassword = ''
    for x in  range(length):
        thepassword += random.choice(characters)


    return render(request, 'generator/password.html',{'password':thepassword})