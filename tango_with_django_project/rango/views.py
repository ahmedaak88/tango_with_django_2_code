from django.shortcuts import render
from django.http import HttpResponse
def index(request):
	#Construct a dictionary to pass to the template engine as its context.
	#Note the key boldmessage matches to {{ boldmessage }} in the tempalte
	context_dict = {'boldmessage':'crunchy , creamy , cookie , candy , cupcake'}
	return render(request, 'rango/index.html' , context=context_dict)

def about(request):
	context_dict = {'myname':'ahmad ali'}
	return render(request,'rango/about.html',context=context_dict)
	