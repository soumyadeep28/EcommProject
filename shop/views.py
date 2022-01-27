from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request , 'shop/index.html')

def about(request):
    return HttpResponse('We are in about')

def contacts(request):
    return HttpResponse('We are in contacts')

def tracker(request):
    return HttpResponse('We are in tracker')

def search(request):
    return HttpResponse('We are in search')

def products(request):
    return HttpResponse('We are in productscheckout')

def checkout(request):
    return HttpResponse('We are in checkout')