from django.shortcuts import render

# Create your views here.
from django.contrib import auth,messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from bankapp import views
from django.urls import reverse_lazy


# Create your views here.
def login(request):
    if request.method == 'POST':
        usrnme=request.POST['username']
        paswrd=request.POST['password']
        user=auth.authenticate(username=usrnme,password=paswrd)
        if user is not None:
            auth.login(request,user)
            return redirect('/newpage')
        else:
            messages.info(request,'invalid user')
            return redirect('credentials:login')
    return render(request,'login.html')


def register(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        cpassword=request.POST['cpassword']

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username already exists')
                return redirect('./register')

            else:
                user=User.objects.create_user(username=username,password=password)
                user.save()
                return redirect('login/')

        else:
            messages.info(request,'Passwoed doesnt matching')
            return redirect('./register')
        return redirect('/')

    return render(request,'register.html')

# def profile(request):
#     return render(request,'profilehome.html')
#


def logout(request):
    auth.logout(request)
    return redirect('/')

