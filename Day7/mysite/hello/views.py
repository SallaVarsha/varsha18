from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
def demo(request):
    temp=loader.get_template('prg1.html')
    return HttpResponse(temp.render())
# Create your views here.
