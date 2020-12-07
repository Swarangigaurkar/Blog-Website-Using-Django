from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.

def register(request):
    flag = 0
    if request.method=='POST':
        uname=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        emaill=request.POST['emaill']
        passwords=request.POST['passwords']
        cpasswords=request.POST['confirmpassword']

        if passwords==cpasswords :
            if User.objects.filter(username=uname).exists() or User.objects.filter(email=emaill).exists() :
                messages.info(request,'Username or Email already taken :(')
                return redirect('register')
            else:
                user = User.objects.create_user(username=uname,password=passwords,email=emaill,first_name=fname,last_name=lname)
                user.save()
                user = auth.authenticate(username=uname ,password=passwords)
                if user is not None:
                    auth.login(request,user)
                    return redirect('/')
        else :
            messages.info(request,'Please enter the same passwords!!')
            return redirect('register')
            
    else:
        return render(request,'temp3.html')


def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user = auth.authenticate(username=username ,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Incorrect Credentials')
            return redirect('login')

    else:
        return render(request,'temp4.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
