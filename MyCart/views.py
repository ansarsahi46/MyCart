from django.shortcuts import render
from django.http import HttpResponse


#index function

def index(request):
    return render(request, 'index.html')
