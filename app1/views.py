from django.shortcuts import render

# Create your views here.

def world(request):
    return render(request,'world.html')



def environment(request):
    return render(request,'environment.html')