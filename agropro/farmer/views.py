from django.shortcuts import render, redirect
from django.apps import apps
Farmer = apps.get_model('home', 'Farmer')
Wholesaler = apps.get_model('home', 'Wholesaler')
Crop = apps.get_model('home', 'Crop')
Notification = apps.get_model('home', 'Notification')

# Create your views here.
def prediction(request):
    if request.user.is_authenticated:
        utype=request.user.username
        utype=utype[utype.rfind('-')+1:]
        context={'utype':utype,'username':request.user.username[:request.user.username.rfind('-')]}
        return render(request,'predic.html',context)
    else:
        return redirect('/login')

def notification(request):
    if request.user.is_authenticated:
        utype=request.user.username
        utype=utype[utype.rfind('-')+1:]

        if request.method=='POST':
            not_id=request.POST['id']
            notif_obj=list(Notification.objects.filter(id=not_id))[0]
            notif_obj.accepted=True
            notif_obj.save()

        f_obj=list(Farmer.objects.filter(username=request.user.username))[0]
        notif_final=[]
        notif_temp=list(Notification.objects.all())
        for i in notif_temp:
            if i.crop.farmer.id == f_obj.id:
                notif_final.append([])
                notif_final[-1].append(i.crop.name)
                notif_final[-1].append(i.wholesaler.name)
                notif_final[-1].append(i.crop.price)
                notif_final[-1].append(i.accepted)
                notif_final[-1].append("91"+i.wholesaler.phone)
                notif_final[-1].append(i.id)
        print(notif_final)

        # Order By
        ob=request.GET.get('orderby')
        if ob=="Pending":
            crops=sorted(notif_final, key=lambda x: x[3])
        if ob=="Accepted":
            crops=(sorted(notif_final, key=lambda x: x[3])).reverse()

        context={'utype':utype,'username':request.user.username[:request.user.username.rfind('-')],"notif":notif_final,"n":3}
        return render(request,'notif.html',context)
    else:
        return redirect('/login')
    

def profile(request):
    if request.user.is_authenticated:
        utype=request.user.username
        utype=utype[utype.rfind('-')+1:]
        context={'utype':utype,'username':request.user.username[:request.user.username.rfind('-')]}
        return render(request,'profile.html',context)
    else:
        return redirect('/login')
