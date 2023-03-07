from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.shortcuts import render,redirect

from Backend.models import admindb, categorydb, productdb,contactdb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError

from Frontend.models import checkoutdb


# Create your views here.

def indexpage(request):
    return render(request,"index.html")

def addadmin(request):
    return render(request,"addadmin.html")

def saveadmin(request):
    if request.method == "POST":
        na = request.POST.get('name')
        em = request.POST.get('email')
        un = request.POST.get('username')
        password = request.POST.get('password')
        img = request.FILES['image']
        obj = admindb(Name=na, Email=em,Username=un,  Password=password, Image=img)
        obj.save()
        return redirect(addadmin)

def admindisplay(request):
    data = admindb.objects.all()
    return render(request,"displayAdmin.html",{'data':data})

def editadminpage(req,dataid):
    data = admindb.objects.get(id=dataid)
    print(data)
    return render(req,"editadmin.html", {'data':data})
def updateadmin(req,dataid):
    if req.method == "POST":
        na = req.POST.get('name')
        email = req.POST.get('email')
        un = req.POST.get('username')
        passwrd = req.POST.get('password')
        try:
            img = req.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = admindb.objects.get(id=dataid).Image
        admindb.objects.filter(id=dataid).update(Name=na, Email=email,Username=un, Password=passwrd, Image=file)
        return redirect(admindisplay)

def deleteadmin(req,dataid):
    data = admindb.objects.filter(id=dataid)
    data.delete()
    return redirect(admindisplay)

def category(req):
    return render(req,"addcategory.html")

def savecategory(request):
    if request.method == "POST":
        na = request.POST.get('name')
        de = request.POST.get('description')
        im = request.FILES['image']
        obj=categorydb(Name=na,Description=de,Image=im)
        obj.save()
        return redirect(category)

def categorydisplay(req):
    data = categorydb.objects.all()
    return render(req,"displaycategory.html",{'data':data})


def editcategory(req,dataid):
    data = categorydb.objects.get(id=dataid)
    return render(req,"editcategory.html",{'data':data})
def updatecategory(req,dataid):
    if req.method =="POST":
        na = req.POST.get('name')
        dis = req.POST.get('description')
        try:
            img = req.FILES['image']
            fs=FileSystemStorage()
            file =fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=categorydb.objects.get(id=dataid).IMAGE
        categorydb.objects.filter(id=dataid).update(Name=na, Description=dis, Image=file)
        return redirect(categorydisplay)

def deletecategory(req,dataid):
    data = categorydb.objects.filter(id=dataid)
    data.delete()
    return redirect(categorydisplay)

def product(req):
    data= categorydb.objects.all()
    return render(req,"addproduct.html",{'data':data})


def productsave(req):
    if req.method == "POST":
        na = req.POST.get('name')
        ca= req.POST.get('category')
        de = req.POST.get('description')
        qu= req.POST.get('quantity')
        pr = req.POST.get('price')
        im= req.FILES['image']
        obj = productdb(Name=na,Category=ca,Description=de,Quantity=qu,Price=pr,Image=im)
        obj.save()
        return redirect(product)


def productdisplay(request):
    data = productdb.objects.all()
    return render(request,"displayproduct.html",{'data':data})


def editproduct(req,dataid):
    data = productdb.objects.get(id=dataid)
    da = categorydb.objects.all()
    return render(req,"editproduct.html",{'data':data, 'da':da})
def updateproduct(req,dataid):
    if req.method =="POST":
        na = req.POST.get('name')
        ca = req.POST.get('category')
        de = req.POST.get('description')
        qu = req.POST.get('quantity')
        pr = req.POST.get('price')
        try:
            img = req.FILES['image']
            fs=FileSystemStorage()
            file =fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=productdb.objects.get(id=dataid).Image
        productdb.objects.filter(id=dataid).update(Name=na,Category=ca,Description=de,Quantity=qu,Price=pr,Image=file)
        return redirect(productdisplay)

def deleteproduct(req,dataid):
    data = productdb.objects.filter(id=dataid)
    data.delete()
    return redirect(productdisplay)

def loginpage(req):
    return render(req,"login.html")

def adminlogin(req):
    if req.method == "POST":
        username_r = req.POST.get('username')
        password_r = req.POST.get('password')

        if admindb.objects.filter(Username=username_r, Password=password_r).exists():
            req.session['username'] = username_r
            req.session['password'] = password_r
            messages.success(req, "Login Successfully...!")

            return redirect(indexpage)
        else:
            messages.error(req,"Invalid User..!")

            return render(req, "login.html")

def adminlogout(request):
    del request.session['username']
    del request.session['password']
    messages.success(request, "Logout Successfully...!")
    return redirect(loginpage)

def displaymessage(req):
    data=contactdb.objects.all()
    return render(req,"displaycontactus.html",{'data':data})

def deletemessage(req,dataid):
    data = contactdb.objects.filter(id=dataid)
    data.delete()
    return redirect(displaymessage)

def orders(req):
    data = checkoutdb.objects.all()
    return render(req,"displayorder.html",{'data':data})

def deleteorder(req,dataid):
    data = checkoutdb.objects.filter(id=dataid)
    data.delete()
    return redirect(orders)



