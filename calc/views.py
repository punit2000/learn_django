from django.db.models.expressions import result
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html',{'name':'Punit'})

def add(request):
    val1 = int(request.POST["num1"])
    val2 = int(request.POST["num2"])
    res = val1 +val2
    return render(request,'result.html', {'result':res})


