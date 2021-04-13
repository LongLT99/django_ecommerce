from django.shortcuts import render
from .models import User
from django.contrib import messages

# Create your views here.
def index(request):
    if request.method == 'POST':
        if request.POST.get('username') and request.POST.get('password'):
            saverecord1 = User()
            saverecord1.username = request.POST.get('username')
            saverecord1.password = request.POST.get('password')
            saverecord1.save()
            messages.success(request,"Success")
            return render(request,"register.html")
    else:
        return render(request,"register.html")

