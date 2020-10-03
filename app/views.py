from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# responding a string by using FBV
from app.forms import *

from django.views.generic import View,TemplateView

def function1(request):
    return HttpResponse('This is a FBV')

# responding a string by using CBV

class CBV(View):
    def get(self,request):
        return HttpResponse('This Is A CBV')

# responding an HTML file by using FBV

def FBV_template(request):
    return render(request,'FBV_template.html',context={'name':'PYTHON'})


# responding an HTML file by using CBV


class CBV_template(View):
    def get(self,request):
        return render(request,'CBV_template.html',context={'name':'Django'})

# validating the form by using FBV

def FBV_form(request):
    form=Student()
    if request.method=='POST':
        form_data=Student(request.POST)
        if form_data.is_valid():
            return HttpResponse(form_data.cleaned_data['name'])
    return render(request,'FBV_form.html',context={'form':form})

# validating the form by using CBV

class CBV_form(View):
    def get(self,request):
        form=Student()
        return render(request,'CBV_form.html',context={'form':form})

    def post(self,request):
        form_data=Student(request.POST)
        if form_data.is_valid():
            return HttpResponse(form_data.cleaned_data['name'])


    
class template_view(TemplateView):
    template_name='CBV_template.html'



