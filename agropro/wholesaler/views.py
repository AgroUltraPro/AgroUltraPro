from django.shortcuts import render

# Create your views here.
def market(request):
    return render(request,'market.html')

def notification(request):
    return render(request,'notif.html')

def profile(request):
    return render(request,'profile.html')
