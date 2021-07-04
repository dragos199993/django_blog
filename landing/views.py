from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  context = {
    'name': 'Dragos',
    'age': 28
  }
  return render(request, 'index.html', context)
