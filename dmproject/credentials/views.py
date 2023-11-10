from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid credentials')
            return redirect('login')


    return render(request,"login.html")


def registeration(request):
    if request.method== 'POST':
        user_name = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=user_name).exists():
                messages.info(request,"Username taken")
                return redirect('registeration')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email taken")
                return redirect('registeration')
            else:
                user=User.objects.create_user(username=user_name,password=password,first_name=first_name,last_name=last_name,email=email)
                user.save()
                # print("User created")
                return redirect('login')
        else:
            messages.info(request,"Password not mathing")
    return render(request,"registerations.html")
def logout(request):
    auth.logout(request)
    return redirect('/')