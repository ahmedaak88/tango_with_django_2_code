from django.shortcuts import render
from django.http import HttpResponse
def index(request):
	return HttpResponse("Rango say hey there partner")
def about(request):
	return HttpResponse("About page")
	pass