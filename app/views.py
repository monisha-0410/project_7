from django.shortcuts import render

# Create your views here.
def print(request):
    d={'Name':"Rajkumar"}
    return render(request,'print.html',d)