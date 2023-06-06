from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def hello(request):
      return render(request, 'auth_system/hello.html')


def Reg(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        name = request.POST.get('Username')
        password = request.POST.get('psw')

        new_user = User.objects.create_user(name,email, password)
        

        new_user.save()
        return redirect('log-page')
    return render(request, 'auth_system/reg.html')

def log(request):
      if request.method == 'POST':
        name = request.POST.get('Username')
        password = request.POST.get('psw')

        user = authenticate(request, username=name, password=password)
        if user is not None:
            login(request, user)
            return redirect('hello-page')
        else:
            return HttpResponse('Error, user does not exist')
      return render(request, 'auth_system/log.html')
