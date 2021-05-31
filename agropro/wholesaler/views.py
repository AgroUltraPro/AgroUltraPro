from django.shortcuts import render,redirect
from django.apps import apps
import math
Farmer = apps.get_model('home', 'Farmer')
Wholesaler = apps.get_model('home', 'Wholesaler')
Crop = apps.get_model('home', 'Crop')
Notification = apps.get_model('home', 'Notification')

# Create your views here.
def market(request):
    if request.user.is_authenticated:
        
        utype=request.user.username
        utype=utype[utype.rfind('-')+1:]
        if request.method =="POST":
            # print("Hemlo                                       ***************              ",request.user.username[:request.user.username.rfind('-')])
            wh_ob=list(Wholesaler.objects.filter(username=request.user.username))[0]
            c_id=request.POST["id"]
            crop_obj=list(Crop.objects.filter(id=c_id))[0]
            notif=Notification(crop=crop_obj,wholesaler=wh_ob,accepted=False,interested=True)
            notif.save()


        qr=list(Crop.objects.all())
        # print (crops)
        crops=[]
        for i in qr:
            if i.available:
                crops.append([])
                crops[-1].append(i.name)
                crops[-1].append(i.quantity)
                crops[-1].append(i.price)
                crops[-1].append(i.farmer.name)
                wh_ob=list(Wholesaler.objects.filter(username=request.user.username))[0]
                notif_int=False
                notif_acc=True
                if len(list(Notification.objects.filter(crop=i,wholesaler=wh_ob))):
                    notif_int=True
                    notif_acc=list(Notification.objects.filter(crop=i,wholesaler=wh_ob))[0].accepted
                crops[-1].append(notif_int)
                crops[-1].append(notif_acc)
                crops[-1].append(i.id)
                crops[-1].append(i.created)
        
        print(crops)
        # Order By
        ob=""
        if request.GET.get('orderbyname') is not None:
            ob=request.GET.get('orderbyname')
        if ob=="Name":
            crops=sorted(crops, key=lambda x: x[0])
        if ob=="Date":
            crops=sorted(crops, key=lambda x: x[-1])
        
        for i in crops:
            del i[-1]
        
        # Filter
        fname=""
        fcrop=""
        fqty=10000
        fprice=0

        if request.GET.get('name') is not None:
            fname=request.GET.get('name')
        if request.GET.get('crop') is not None:
            fcrop=request.GET.get('crop')
        if request.GET.get('qty') is not None:
            fqty=int(request.GET.get('qty'))
        if request.GET.get('price') is not None:
            fprice=int(request.GET.get('price'))
        
        print(fname, fcrop, fqty, fprice)
        cropscpy=crops.copy()
        crops=[]
        dele=[]
        # All 4 matching
        print("in for 4")
        print(cropscpy)
        for i in cropscpy:
            
            if  i[0].find(fcrop)!=-1 and i[3].find(fname)!=-1 and fqty<=i[1] and fprice>=i[2]:
                print("in if")
                print(i)
                crops.append(i)
                dele.append(i)
        for i in dele:
            cropscpy.remove(i)
        dele=[]
        print (cropscpy)
        # Any 3 Matching
        print("in for 3")
        for i in cropscpy:
            if (i[0].find(fcrop)!=-1 and i[3].find(fname)!=-1 and fqty<=i[1]) or (i[0].find(fcrop)!=-1 and i[3].find(fname)!=-1 and  fprice>=i[2]):
                crops.append(i)
                dele.append(i)
            if (i[0].find(fcrop)!=-1 and fprice>=i[2] and fqty<=i[1]) or (fprice>=i[2] and i[3].find(fname)!=-1 and fqty<=i[1]):
                crops.append(i)
                dele.append(i)
        for i in dele:
            cropscpy.remove(i)
        dele=[]
        # Any 2 Matching
        print("in for 2")
        for i in cropscpy:
            if (i[0].find(fcrop)!=-1 and i[3].find(fname)!=-1) or (i[0].find(fcrop)!=-1 and fprice>=i[2]) or (i[3].find(fname)!=-1 and fprice>=i[2]):
                crops.append(i)
                dele.append(i)
            if (i[0].find(fcrop)!=-1 and fqty<=i[1]) or (i[3].find(fname)!=-1 and fqty<=i[1]) or (fprice>=i[2] and fqty<=i[1]):
                crops.append(i)
                dele.append(i)
        for i in dele:
            cropscpy.remove(i)
        dele=[]
        # Any 1 matching
        print("in for 1")
        for i in cropscpy:
            print("in for")
            if  i[0].find(fcrop)!=-1 or i[3].find(fname)!=-1 or fqty<=i[1] or fprice>=i[2]:
                print(i)
                crops.append(i)
        print (cropscpy)
        print("*************************************************",crops)
        f=[fname,fcrop,fqty,fprice]
        # finalcrops=[]
        # for i in range(len(crops)):
        #     if i%3==0:
        #         finalcrops.append[[]]
        #     finalcrops[-1].append(crops[i])

        
        context={'utype':utype,'username':request.user.username[:request.user.username.rfind('-')],"result":crops,'n':len(crops),"filter":f,"r":range(len(crops))}
        return render(request,'market.html',context)
    else:
        return redirect('/login')
    

def notification(request):
    if request.user.is_authenticated:
        utype=request.user.username
        utype=utype[utype.rfind('-')+1:]

        w_obj=list(Wholesaler.objects.filter(username=request.user.username))[0]
        notif_final=[]
        notif_temp=list(Notification.objects.filter(wholesaler=w_obj))
        for i in notif_temp:
                notif_final.append([])
                notif_final[-1].append(i.crop.name)
                notif_final[-1].append(i.crop.farmer.name)
                notif_final[-1].append(i.crop.price)
                notif_final[-1].append(i.accepted)
                notif_final[-1].append("91"+i.crop.farmer.phone)
                notif_final[-1].append(i.id)
        print(notif_final)

        # Order By
        ob=request.GET.get('orderby')
        if ob=="Pending":
            crops=sorted(notif_final, key=lambda x: x[3])
        if ob=="Accepted":
            crops=(sorted(notif_final, key=lambda x: x[3])).reverse()


        context={'utype':utype,'username':request.user.username[:request.user.username.rfind('-')],"notif":notif_final,"n":4}
        return render(request,'notif.html',context)
    else:
        return redirect('/login')
    

def profile(request):
    if request.user.is_authenticated:
        username=request.user.username
        username=username[:username.rfind('-')]
        # context={'utype':utype,'username':request.user.username[:request.user.username.rfind('-')+1]}
        print(username,"Ho raha hai")
        instance = Wholesaler.objects.filter(username = request.user.username).values()[0]
        # crops = Crop.objects.filter(whole = instance['id'],available = True).values()
        
        print("The instance is:",instance)
        # print("The crop instance  is:",crops)
        context = {
            'instance':instance
            # 'crops':crops
        }

        return render(request,'profileWhole.html',context = context)
    else:
        return redirect('/')


def editProfile(request):
    if request.method == 'POST' and request.user.is_authenticated:
        username=request.user.username
        username=username[:username.rfind('-')]
        # context={'utype':utype,'username':request.user.username[:request.user.username.rfind('-')+1]}
        print(username,"Ho raha hai")
        instance = Wholesaler.objects.filter(username = request.user.username).update(name = request.POST['name'],state = request.POST['state'],email = request.POST['email'],address = request.POST['address'],phone = request.POST['phone'])
        
        print("The instance is:",instance)
        print("The new changes are:",request.POST['state'],request.POST['name'],request.POST['phone'],request.POST['email'],request.POST['address'])

        # instance['name'] = request.POST['name']
        # instance['phone'] = request.POST['phone']
        # instance['area'] = request.POST['area']
        # instance['state'] = request.POST['state']
        # instance['address'] = request.POST['address']
        # instance['email'] = request.POST['email']
        # instance.save()
        # context = instance
        return redirect('/wholesaler/profile')

