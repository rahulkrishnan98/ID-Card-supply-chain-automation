from django.shortcuts import render
from .forms import ClientDetailForm, RegisterUser
from django.http import HttpResponse, HttpResponseRedirect
from .models import ClientDetail, OrderDetail, Uploadtemplate
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = RegisterUser(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect('/addorder/')
    else:
        form = RegisterUser()
    context = {
        'form':form
    }
    return render(request,'signup.html',context)

def dashboard(request):
    total = OrderDetail.objects.count()
    pending = OrderDetail.objects.filter(template=True,data=True,billing=True,production=True,shipping=True).count()
    context = {
        'total':total,
        'pending':total - pending,
    }
    return render(request,'dashboard.html',context)

def registerclient(request):
    form = ClientDetailForm()
    if request.method == 'POST':
        form2 = ClientDetailForm(request.POST)
        print(form2.is_valid())
        if form2.is_valid():
            obj = form2.save(commit=False)
            obj.save()
            return HttpResponseRedirect('/registerclient/')
    context = {
        'form':form
    }
    return render(request,'registerclient.html',context)

def clientdetails(request):
    if request.method == "POST":
        addorder = request.POST.get('addorder')
        obj = ClientDetail.objects.get(company=addorder)
        order = OrderDetail(company=obj)
        order.save()

        return HttpResponseRedirect('/clientdetails/'+addorder+'/')
    obj = ClientDetail.objects.all()
    context = {
        'detail':obj
    }
    return render(request,'clientdetails.html',context)

def clientpage(request,client):
    print(client)
    obj = OrderDetail.objects.filter(Q(company__company__iexact=client))
    comp = ClientDetail.objects.get(company__iexact=client)
    print(comp)
    num = len(obj)
    if len(obj) == 0:
        obj = None
        num = 0
    context = {
        'detail':obj,
        'client':client,
        'num':num,
        'comp':comp,
    }
    return render(request,'clientpage.html',context)

def orderlists(request):
    total = OrderDetail.objects.count()
    pending = OrderDetail.objects.filter(template=True,data=True,billing=True,production=True,shipping=True).count()
    obj = OrderDetail.objects.all()
    context = {
        'total':total,
        'pending':total - pending,
        'detail':obj
    }
    return render(request,'orderlist.html',context)

def orderlistfilter(request,slug,stage):
    if request.method == "POST":
        # ProfileForm(request.POST, request.FILES)
        # order = OrderDetail.objects.get(orderid=slug)
        # image1 = request.POST.get('image1')
        # print(image1)
        # # obj = Uploadtemplate()
        # # obj.orderid = order
        # # obj.fimage = image1
        # # # obj.bimage = image2
        # # obj.save()
        return HttpResponseRedirect("/orderlist/"+str(slug)+"/template")
    total = OrderDetail.objects.count()
    if slug.lower() == 'pending':
        print(slug.lower())
    elif slug is not None:
        order = OrderDetail.objects.get(orderid=slug)
        context = {
            'order':order,
            'fimage':False,
            'bimage':False,
        }
        if Uploadtemplate.objects.filter(orderid=order).count() != 0:
            image1 = Uploadtemplate.objects.get(orderid=order)
            image2 = Uploadtemplate.objects.get(orderid=order)
            context = {
                'order':order,
                'fimage':image1.fimage,
                'bimage':image2.bimage,
            }
        return render(request,'tempupload.html',context)
    pending = OrderDetail.objects.filter(template=True,data=True,billing=True,production=True,shipping=True).count()
    obj = OrderDetail.objects.exclude(template=True,data=True,billing=True,production=True,shipping=True)
    context = {
        'total':total,
        'pending':total - pending,
        'detail':obj
    }
    return render(request,'orderlist.html',context)

# def uploadtemplate(stage):
