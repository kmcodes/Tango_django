from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response

# Create your views here.
from django.http import HttpResponse

def index(request):
    context = RequestContext(request)    
    context_dict = {'boldmessage': "I am bold font from the context"}    
    return render_to_response('rango/index.html', context_dict, context)
    
def about(request):
    return HttpResponse("Rango says: Hello world! <a href='/rango/'>Rango</a>")