from django.shortcuts import render

def home(request):
    return render(request,'pizza/home.html')
