from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as authlogin
from .models import Farmer, Wholesaler

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        utype=request.user.username
        utype=utype[utype.rfind('-')+1:]
        context={'utype':utype,'username':request.user.username[:request.user.username.rfind('-')+1]}
        print(request.user.username,utype,"Ho raha hai")
    else:
        context={'utype':None,'username':None}
    return render(request,'main.html',context)

def login(request):
    # print("Hemlo")
    # if request.method == 'POST':
    #     print("Hemlo2")
    #     password1= request.POST['password']
    #     utype = request.POST['usertype']
    #     username= request.POST['username']
    #     print("***",username,password1,utype,"***")
    #     return redirect('/')
    # else:    
    return render(request,'login.html')

def signin(request):
    print("Hemlo")
    if request.method == 'POST':
        print("Hemlo2")
        password1= request.POST['password']
        utype = request.POST['usertype']
        username= request.POST['username']+"-"+utype
        print("***",username,password1,utype,"***")
        user=authenticate(username=username,password=password1)
        if user is not None:
            authlogin(request,user)
            print(user)
        return redirect('/')

def signup(request):
    if request.method == 'POST':
        name= request.POST['fullname']
        
        phone= request.POST['phone number']
        password1= request.POST['confirmpassword']
        #password2= request.POST['']
        utype = request.POST['usertype']
        username= request.POST['username']+"-"+utype
        fname,lname=name.split(' ')
        print("***",name,username,phone,password1,utype,"***")

        #Check the inputs
        # if utype=='farmer':
        #     # farmer=Farmer(email=username,phone=phone,password=password1)
        #     #farmer.save()
        # if utype=='wholesaler':
        #     # ws=Wholesaler(email=username,phone=phone,password=password1)
        #     #ws.save()

        # #Creating User
        user=User.objects.create_user(username,email=None,password=password1,first_name=fname,last_name=lname)
        return redirect('/login')

def market(request):
    return render(request,'market.html')

def prediction(request):
    return render(request,'predic.html')

def notification(request):
    return render(request,'notif.html')

def profile(request):
    return render(request,'profile.html')
