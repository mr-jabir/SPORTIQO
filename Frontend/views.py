from django.contrib import messages
from django.shortcuts import render,redirect
from Backend.models import categorydb,productdb,contactdb
from Frontend.models import customerdb, cartdb,checkoutdb


# Create your views here.
def homepage(req):
    data = categorydb.objects.all()
    return render(req, "home.html", {'data': data})

def contactpage(req):
    return render(req,"contact.html")

def categorypage(req):
    data = categorydb.objects.all()
    return render(req,"categories.html",{'data': data})

def disproduct(request,itemcatg):
    print("===itemcatg===", itemcatg)
    catg = itemcatg.upper()

    products = productdb.objects.filter(Category=itemcatg)
    context = {
        'products': products,
        'catg': catg
    }
    return render(request,"product.html",context)


def productsingle(request,dataid):
    data=productdb.objects.get(id=dataid)
    return render(request,"singleproduct.html",{'dat':data})

def savecontactus(req):
    if req.method=="POST":
        na = req.POST.get('name')
        em = req.POST.get('email')
        sb = req.POST.get('subject')
        ms = req.POST.get('message')
        obj = contactdb(Name=na,Email=em,Subject=sb,Message=ms)
        obj.save()
        messages.success(req, "Message sent")

        return redirect(contactpage)

def weblogin(req):
    return render(req,"weblogin.html")

def savecustomer(request):
    if request.method == "POST":
        Us  = request.POST.get('username')
        Em = request.POST.get('email')
        pas = request.POST.get('password')
        Cp  = request.POST.get("conpassword")
        if pas==Cp:
            obj = customerdb(Username=Us,Password=pas,Confirmpassword=Cp,Email=Em,)
        obj.save()
        messages.success(request, "Registered Successfully")

        return redirect(weblogin)

def custemerlogin(request):
    if request.method=='POST':
        Username_r=request.POST.get("username")
        Password_r=request.POST.get("password")

        if customerdb.objects.filter(Username=Username_r,Password=Password_r).exists():
            request.session['username']=Username_r
            request.session['password']=Password_r
            messages.success(request, "Login Successfully...!")
            return redirect(homepage)
        else:
            messages.error(request,"Invalid User..!")
            return render(request,'weblogin.html')

def logout(request):
    del request.session['username']
    del request.session['password']
    messages.success(request, "Logout Successfully...!")
    return redirect(weblogin)



def savecart(req):
    if req.method=="POST":
        pna = req.POST.get('prodname')
        cat = req.POST.get('procart')
        qty= req.POST.get('quantity')
        tprice = req.POST.get('totalprice')
        obj = cartdb(Proname=pna,Category=cat,Quantity=qty,Price=tprice)
        obj.save()
        messages.success(req, "Added to Cart")
        return redirect(homepage)

def viewcartpage(req):
    data = cartdb.objects.all()
    return render(req,"addcart.html",{'data':data})

def deletecartfont(req,dataid):
    data = cartdb.objects.get(id=dataid)
    data.delete()
    return redirect(viewcartpage)

def check(req):
    data = cartdb.objects.all()
    return render(req,"checkout.html",{'data':data})

def savecheck(req):
    if req.method=="POST":
        na = req.POST.get('name')
        em = req.POST.get('email')
        add= req.POST.get('address')
        pi = req.POST.get('pincode')
        ph = req.POST.get('phone')
        py= req.POST.get('cname')

        pa = req.POST.get('prodname')
        obj = checkoutdb(Name=na,Email=em,Address=add,Pincode=pi,Phone=ph,CardName=py,Expiration=pa)
        obj.save()
        messages.success(req, "Your order has been placed")

        return redirect(homepage)


