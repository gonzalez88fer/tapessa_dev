from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
def home(request, *args, **kwargs):
    context = {}
    return render(request, 'base.html', context= context)