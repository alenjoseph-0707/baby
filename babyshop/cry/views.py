from django.shortcuts import render
from.models import regform
def index(request):
    return render(request,'index.html')
def shop(request):
    return render(request,'shop.html')
def signup(request):
    if request.method=="POST":
        fname=request.POST.get('fn')
        lname=request.POST.get('ln')
        email=request.POST.get('em')
        mobile=request.POST.get('mn')
        password=request.POST.get('pas')
        obj=regform.objects.create(fn=fname,ln=lname,em=email,mn=mobile,pas=password)
        
        if obj:
            obj.save()
            return render(request,"login.html",{'msg':'success'})
        else:
            return render(request,"signup.html",{'msg':'not '})
    else:
        return render(request,'signup.html')    



def login(request):
    if request.method=="POST":
        email=request.POST.get('eid')
        password=request.POST.get('passw')
        obj=regform.objects.filter(em=email,pas=password)
        
        if obj:
            request.session['eid']=email
            request.session['passw']=password
            
            
            return render(request,"index.html",{'msg':'success'})
        else:
             request.session['eid']=''
             request.session['passw']=''

             return render(request,"login.html",{'msg':'not '})
    else:
            return render(request,'login.html')    

def toys(request):
    return render(request,'babytoys.html')

def fashions(request):
    return render(request,'babyfashion.html')

def foods(request):
    return render(request,'babyfoods.html')

def specials(request):
    return render(request,'specialoffer.html')

def buyones(request):
    return render(request,'buy1.html')

def carts(request):
    return render(request,'cart.html')





      

  


