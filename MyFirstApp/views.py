from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html',)

def add(request):
    val1 = int(request.POST['number1'])
    val2 = int(request.POST['number2'])
    res1 = val1 + val2
    return render(request, 'home.html',{'result1':res1})

def sub(request):
    val3 = int(request.GET['number3'])
    val4 = int(request.GET['number4'])
    res2 = val3 - val4
    return render(request, 'home.html',{'result2':res2})