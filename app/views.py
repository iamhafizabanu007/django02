from django.shortcuts import render
from .models import students

# Create your views here.
def home(request):
    return render(request,'base.html')

def html1(request):
    return render(request,'html1.html')

def css(request):
    return render(request,'css.html')

def tables(request):
    obj=students.objects.all()
    return render(request,'tables.html',{'obj':obj})

def images(request):
    return render(request,'images.html')