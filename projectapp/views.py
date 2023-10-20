from django.shortcuts import render,redirect

# Create your views here.


def salom(request):
    ctx ={
        "root":"assalom"
    }

    return render(request,'index.html')