from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def msd(request):
    return render(request,'msd.html')
def macha(request):
    return HttpResponse('<center><h1> CAPTAIN COOL</h1></center>')