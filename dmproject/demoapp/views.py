from django.http import HttpResponse
from django.shortcuts import render
from .models import Place
from .models import Team
# Create your views here.
def hello(request):
    T_obj=Team.objects.all()
    obj=Place.objects.all()
    return render(request,"index.html",{"result":obj,"team":T_obj})
# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     res=x+y
#     return render(request,'add.html',{"result":res})