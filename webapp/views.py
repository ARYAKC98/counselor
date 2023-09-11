from django.shortcuts import render,redirect
from webapp.models import userregister_db
# Create your views here.
def home_page(req):
    return render(req,'home.html')


def register_page(req):
    return render(req,'register.html')

def save_regdb(request):
    if request.method=="POST":
        na = request.POST.get('name')
        mail = request.POST.get('email')
        pas = request.POST.get('pass')
        obj=userregister_db(uname=na,uemail=mail,upass=pas,)
        obj.save()
        return redirect(register_page)

def userlogin(request):
    if request.method=="POST":
        uname = request.POST.get('username')
        pwd = request.POST.get('password')
        if userregister_db.objects.filter(uname=uname,upass=pwd).exists():
            request.session['username']=uname
            request.session['password']=pwd

            return redirect(home_page)
        else:
            return redirect(register_page)

    return redirect(register_page)

def user_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(register_page)


def about_page(req):
    return render(req,'about.html')

def counselor_page(req):
    return render(req,'counselor.html')


def service_page(req):
    return render(req,'service.html')

def price_page(req):
    return render(req,'price.html')

def blog_page(req):
    return render(req,'blog.html')

def contact_page(req):
    return render(req,'contact.html')

def single_page(req):
    return render(req,'single.html')