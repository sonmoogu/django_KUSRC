from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = {}
    return render(request, 'index.html', context)

def one_one(request):
    context = {}
    return render(request, '1-1.html', context)

def one_two(request):
    context = {}
    return render(request, '1-2.html', context)

def two_one(request):
    context = {}
    return render(request, '2-1.html', context)

def two_two(request):
    context = {}
    return render(request, '2-2.html', context)

def two_three(request):
    context = {}
    return render(request, '2-3.html', context)

def five_one(request):
    context = {}
    return render(request, '5-1.html', context)

