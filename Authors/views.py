from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the authors page")
# Create your views here.

def detail():
	pass