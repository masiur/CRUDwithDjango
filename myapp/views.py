import datetime  
# Create your views here.  
from django.http import HttpResponse  
from django.shortcuts import render

def index(request):
    template_name = 'index.html'
    context = {'nowFromViewFile': datetime.datetime.now()} 
    return render(request, template_name, context)