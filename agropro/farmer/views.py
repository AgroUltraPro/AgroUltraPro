from django.shortcuts import render

# Create your views here.
def prediction(request):
    return render(request,'predic.html')

def notification(request):
    return render(request,'notif.html')

def profile(request):
    return render(request,'profile.html')
