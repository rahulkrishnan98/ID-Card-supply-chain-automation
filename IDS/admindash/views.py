from django.shortcuts import render
from .forms import ClientDetailForm, RegisterUser, UploadTemplateForm
from django.http import HttpResponse, HttpResponseRedirect
from .models import ClientDetail, OrderDetail, Uploadtemplate, GetData
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
import os
from django.conf import settings
from django.http import HttpResponse, Http404

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
        order = OrderDetail.objects.get(orderid=slug)
        form = UploadTemplateForm(request.POST, request.FILES)
        form.orderid = order
        if form.is_valid():
            print(form)
            form.save()
            return HttpResponseRedirect("/orderlist/"+str(slug)+"/template")
    total = OrderDetail.objects.count()
    if stage.lower() == 'pending':
        print(slug.lower())
    elif stage.lower() == 'template':
        return render(request,'tempupload.html',uploadtemplate(slug))
    elif stage.lower() == 'data':
        # order = OrderDetail.objects.get(orderid=slug)
        # path = GetData.objects.get(orderid=order)
        # file_path = os.path.join(settings.STATIC_ROOT, str(path.file))
        # if os.path.exists(file_path):
        #     with open(file_path, 'rb') as fh:
        #         response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
        #         response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
        #         return response
        return render(request,'getdata.html',downloaddata(slug))
    elif stage.lower() == 'billing':
        return render(request,'billing.html',uploadtemplate(slug))
    elif stage.lower() == 'production':
        return render(request,'production.html',uploadtemplate(slug))
    elif stage.lower() == 'shipping':
        return render(request,'shipping.html',uploadtemplate(slug))
    pending = OrderDetail.objects.filter(template=True,data=True,billing=True,production=True,shipping=True).count()
    obj = OrderDetail.objects.exclude(template=True,data=True,billing=True,production=True,shipping=True)
    context = {
        'total':total,
        'pending':total - pending,
        'detail':obj
    }
    return render(request,'orderlist.html',context)

def uploadtemplate(slug):
    order = OrderDetail.objects.get(orderid=slug)
    form = UploadTemplateForm()
    context = {
        'order':order,
        'fimage':False,
        'bimage':False,
        'form':form,
        'response':False
    }
    if Uploadtemplate.objects.filter(orderid=order).count() != 0:
        obj = Uploadtemplate.objects.get(orderid=order)
        response = Uploadtemplate.objects.get(orderid=order)
        context = {
            'form':form,
            'order':order,
            'fimage':obj.fimage,
            'bimage':obj.bimage,
            'response':obj.response
        }
    return context

def downloaddata(slug):
    order = OrderDetail.objects.get(orderid=slug)
    path = GetData.objects.get(orderid=order)
    file_path = os.path.join(settings.STATIC_ROOT, str(path.file))
    # if os.path.exists(file_path):
    #     with open(file_path, 'rb') as fh:
    #         response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
    #         response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
    context = {
        'order':order,
        'file':path.file
    }
    return context
    # if os.path.exists(file_path):
