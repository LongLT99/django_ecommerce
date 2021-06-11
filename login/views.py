from django.shortcuts import render

# Create your views here.
from e_commerce.models import User
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
            return render(request,"login.html")
    else:
        return render(request,"login.html")