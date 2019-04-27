from django.shortcuts import render
from .forms import ClientDetailForm, RegisterOrder
from django.http import HttpResponse, HttpResponseRedirect
from .models import ClientDetail
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = RegisterOrder(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect('/addorder/')
    else:
        form = RegisterOrder()
    context = {
        'form':form
    }
    return render(request,'signup.html',context)

def dashboard(request):
    return render(request,'dashboard.html')

def registerclient(request):
    form = ClientDetailForm()
    if request.method == 'POST':
        form2 = ClientDetailForm(request.POST)
        if form2.is_valid():
            obj = form2.save(commit=False)
            obj.save()
            return HttpResponseRedirect('/registerclient/')
    context = {
        'form':form
    }
    return render(request,'registerclient.html',context)

def clientdetails(request):
    obj = ClientDetail.objects.all()
    context = {
        'detail':obj
    }
    return render(request,'clientdetails.html',context)

def addorder(request):
    context = {}
    return render(request,'addorder.html',context)

def orderlists(request):
    return render(request,'orderlists.html')
