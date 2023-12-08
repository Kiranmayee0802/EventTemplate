from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'eventapp/index.html')

def corporate(request):
    return render(request,'eventapp/corporate.html')

def wedding(request):
    return render(request,'eventapp/wedding.html')

def birthday(request):
    return render(request,'eventapp/birthday.html')