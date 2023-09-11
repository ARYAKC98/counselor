from django.shortcuts import render,redirect
from myapp.models import counselor_db
from myapp.models import blog_db
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate


# Create your views here.
def index_page(req):
    return render(req,'index.html')

def add_session(req):
    return render(req,'addsession.html')

def display_session(req):
    data=counselor_db.objects.all()
    return render(req,'displaysession.html',{'data':data})

def save_session(request):
    if request.method=="POST":
        na = request.POST.get("name")
        pri = request.POST.get("price")
        img = request.FILES["image"]
        des = request.POST.get("description")
        obj = counselor_db(name=na,price=pri,image=img,description=des)
        obj.save()
        return redirect(add_session)

def session_edit(req,dataid):
    data = counselor_db.objects.get(id=dataid)
    return render(req,"editsession.html",{'data':data})


def update_session(request,dataid):
    if request.method=="POST":
        na = request.POST.get("name")
        pri = request.POST.get("price")
        des = request.POST.get("description")
        try:
            img = request.FILES["image"]
            fs = FileSystemStorage()
            file = fs.save(img.name.img)
        except MultiValueDictKeyError:
            file = counselor_db.objects.get(id=dataid).image
            counselor_db.objects.filter(id=dataid).update(name=na,price=pri,image=file,description=des)
        return redirect(display_session)

def delete_session(request,dataid):
    data = counselor_db.objects.filter(id=dataid)
    data.delete()
    return redirect(display_session)

def log(req):
    return render(req,'login.html')

def admin_login(request):
    if request.method == "POST":
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')
        if User.objects.filter(username__contains=uname).exists():

            user = authenticate(username=uname,password=pwd)
            if user is not None:
                login(request,user)
                request.session['username'] = uname
                request.session['password'] = pwd
                return redirect(index_page)
            else:

                return redirect(log)
        else:

            return redirect(log)


def admin_logout(req):
    del req.session['username']
    del req.session['password']
    return redirect(admin_login)

def add_blog(req):
    return render(req,'addblog.html')

def display_blog(req):
    data=blog_db.objects.all()
    return render(req,'displayblog.html',{'data':data})

def save_blog(request):
    if request.method=="POST":
        na = request.POST.get("name")
        img = request.FILES["image"]
        des = request.POST.get("description")
        obj = blog_db(name=na,image=img,description=des)
        obj.save()
        return redirect(add_blog)

def blog_edit(req,dataid):
    data = counselor_db.objects.get(id=dataid)
    return render(req,"editblog.html",{'data':data})


def update_blog(request,dataid):
    if request.method=="POST":
        na = request.POST.get("name")
        des = request.POST.get("description")
        try:
            img = request.FILES["image"]
            fs = FileSystemStorage()
            file = fs.save(img.name.img)
        except MultiValueDictKeyError:
            file = blog_db.objects.get(id=dataid).image
            blog_db.objects.filter(id=dataid).update(name=na,image=file,description=des)
        return redirect(display_blog)

def delete_blog(request,dataid):
    data = blog_db.objects.filter(id=dataid)
    data.delete()
    return redirect(display_blog)