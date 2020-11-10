from django.shortcuts import render
from appsix.models import form_org
from . import forms
# Create your views here.

def index(request):
    return render(request,'index.html')


def form_page(request):
    form = forms.form_new()
    if request.method=='POST':
        form= forms.form_new(request.POST)

        if form.is_valid():
            form.save()
            return index(request)
    return render(request,'form_page.html',{'form':form})


def table(request):
    form_list = form_org.objects.order_by('date')
    return render(request,'table.html',{'form_rec':form_list})