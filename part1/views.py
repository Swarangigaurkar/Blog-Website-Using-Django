from django.shortcuts import render,redirect
from part1.models import Posts,Postsdata
from django.contrib import messages


# Create your views here.

def index(request):
    posts = Postsdata.objects.filter(status=1).order_by('-createdon')
    
    return render(request,'temp1.html',{'post': posts})

def postdetail(request):
    if request.method=='POST':
        pid=request.POST['pid']
        post = Postsdata.objects.filter(id=pid)
        for p in post:
            p.seen_no +=1
            p.save()
        return render(request,'temp2.html',{'post':post})

def createpost(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            title=request.POST['title']
            content=request.POST['content']
            if request.POST.get('publish'):
                status=1
            elif request.POST.get('save'):
                status=0
            pd =Postsdata(uname=request.user,title=title,content=content,status=status)
            pd.save()
            messages.info(request,'Changes Done')
            return redirect('/')
        else:
            return render(request,'temp5.html')
    else:
        return redirect('login')

def profile(request):
    posts = Postsdata.objects.filter(uname=request.user,status=0).order_by('-createdon') 
    return render(request,'temp6.html',{'post': posts})

def editpost(request):
    if request.method=='POST':
        pid=request.POST['pid']
        post = Postsdata.objects.filter(id=pid)
        return render(request,'temp7.html',{'post':post})

def puborsaveeditpost(request):
    if request.method=='POST':
            title=request.POST['title']
            content=request.POST['content']
            pid=request.POST['pid']
            if request.POST.get('publish'):
                status=1
            elif request.POST.get('save'):
                status=0
            pd = Postsdata.objects.get(id = pid)
            pd.title = title
            pd.content = content
            pd.status=status
            pd.save()
            messages.info(request,'Changes Done')
            return redirect('profile')

        