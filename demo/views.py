from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    #return HttpResponse("Hello! world. Welcome to Norato's Home page")
    return render(request, 'website/index.html')

def about(request):
    return HttpResponse("Hello! world. Welcome to Norato's About page")

def contact(request):
    return HttpResponse("Hello! world. Welcome to Norato's Contact Page")