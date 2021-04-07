from django.shortcuts import render
from e_commerce.models import User
from django.contrib import messages

def Userregistration(request):
    if request.method == 'POST':
        if request.POST.get('username') and request.POST.get('password'):
            saverecord1 = User()
            saverecord1.username = request.POST.get('username')
            saverecord1.password = request.POST.get('password')
            saverecord1.save()
            # newuser = User.objects.raw('SELECT * FROM user WHERE Username = %s', [request.POST.get('username')])[0]
            # saverecord2.email = request.POST.get('email')
            # saverecord2.phonenumber = request.POST.get('phonenumber')
            # saverecord2.userid = newuser
            messages.success(request,"Success")
            return render(request,"index.html")
    else:
        return render(request,"index.html")





