from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render,redirect
from django.views import View
from .forms import UserRegisterForm 
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Writer


class Home(View):
    def get(self,request):
        if request.user.is_authenticated:
            return redirect('home:all_writer')
        return render(request,'home/home.html')


class About(View):
    def get(self,request,username):
        return render(request,'home/home.html')

class UserRegisterView(View):
    form_class = UserRegisterForm
    template_class = 'home/register.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home:home')
        return super().dispatch(request, *args, **kwargs)

    def get(self,request):
        form = self.form_class()
        return render(request,self.template_class,{'form':form})
    
    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(username=cd['username'],password=cd['password1'],email=cd['email'])  
            messages.success(request,'user in create!!!')
            return redirect('home:home')
        return render(request,self.template_class,{'form':form})



class WriterView(LoginRequiredMixin,View):
    def get(self,request):
        writers = Writer.objects.all()
        return render(request,'home/writer.html',{'writers':writers})

