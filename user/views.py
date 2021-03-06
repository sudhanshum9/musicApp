from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
# Create your views here.

def index(request):
    return render(request,'user/index.html')

def register(request):
    if request.method =='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account chas been created! You are now able to login {username}!')
            return redirect('/login')
    else:
        form=UserRegisterForm()
    return  render(request,'user/register.html',{'form':form})

def profile(request):
    return  render(request,'user/profile.html')

