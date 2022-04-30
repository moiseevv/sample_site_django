from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse('this is list of advertisement')

	
def vova(request):
	return HttpResponse('he is Vova')
# Create your views here.
