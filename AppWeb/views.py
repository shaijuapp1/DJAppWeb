from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import logout

def userlogout(request):
    logout(request)
    return redirect('home')

