from django.shortcuts import render
from django.contrib import messages
from e_commerce.models import User
from e_commerce.models import Custom
from e_commerce.models import Fullname

# Create your views here.
def index(request):
    if request.method == 'POST':
        if request.POST.get('username') and request.POST.get('password'):
            savefullname = Fullname()
            savefullname.firstname = request.POST.get('firstName')
            savefullname.lastname = request.POST.get('lastName')
            savefullname.save()
            new_name = Fullname.objects.filter(firstname = savefullname.firstname, lastname = savefullname.lastname)
            FullnameID= new_name.get()

            saveuser = User()
            saveuser.username = request.POST.get('username')
            saveuser.password = request.POST.get('password')
            saveuser.fullnameid = FullnameID
            saveuser.save()

            new_user = User.objects.filter(username=saveuser.username,password = saveuser.password )
            userid = new_user.get()

            savecustomer = Custom()
            savecustomer.userid = userid
            savecustomer.email = request.POST.get('email')
            savecustomer.phonenumber = request.POST.get('tel')
            savecustomer.save()

            messages.success(request,"Success")
            return render(request,"register.html")
            
    else:
        return render(request,"register.html")

