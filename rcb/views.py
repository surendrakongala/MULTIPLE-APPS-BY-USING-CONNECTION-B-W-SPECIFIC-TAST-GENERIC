from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def virat(request):
    return render(request,'rcb.html')
def macha1(request):
    return HttpResponse('<h1><center>HELLO HII....</center></h1>')