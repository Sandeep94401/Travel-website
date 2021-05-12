from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'home.html',{'name':'sandeep'})

def add(request):

    val1=int(request.GET["fname"])
    val2=int(request.GET["lname"])
    res=val1 + val2
    return render(request,'result.html',{'result':res})