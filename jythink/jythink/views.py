from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response,render
 
def hello(request):
    return HttpResponse("Hello world ! ")

#Bootstrap test
def test(request):
     return render(request, 'test.html')
