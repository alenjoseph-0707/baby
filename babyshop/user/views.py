from django.shortcuts import render
from .models import adlog

# Create your views here.
def log(request):
    if request.method=="POST":
        email=request.POST.get('eid')
        password=request.POST.get('passw')
        obj=adlog.objects.filter(email=email,password=password)
        
        if obj:
            request.session['eid']=email
            request.session['passw']=password
            
            
            return render(request,"detailadmin.html",{'msg':'success'})
        else:
             request.session['eid']=''
             request.session['passw']=''

             return render(request,"userlogin.html",{'msg':'not '})
    else:
            return render(request,'userlogin.html') 


def addetails(request):
    return render(request,'detailadmin.html')

def userde(request):
    return render(request,'userdet.html')

def stock(request):
    return render(request,'stock.html')

def order(request):
    return render(request,'orderde.html')
