from django.shortcuts import render
from estateapp.models import Member


def register(request):
    if request.method == 'POST':
        member = Member(firstname=request.POST['firstname'], lastname=request.POST['lastname'],
                        email=request.POST['email'],
                        username=request.POST['username'], password=request.POST['password'])
        member.save()

    else:
        return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')


def  index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')

def propertygrid(request):
    return render(request, 'propertygrid.html')

def propertysingle(request):
    return render(request, 'propertysingle.html')

def blog(request):
    return render(request, 'bloggrid.html')

def blogsingle(request):
    return render(request, 'blogsingle.html')

def agentsgrid(request):
    return render(request, 'agentsgrid.html')

def agentsingle(request):
    return render(request, 'agentsingle.html')


def contact(request):
    return render(request, 'contact.html')











