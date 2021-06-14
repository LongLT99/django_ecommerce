from django.shortcuts import redirect, render
from django.contrib import messages
from e_commerce.models import Account, Employee
from e_commerce.models import Customer
from e_commerce.models import Fullname
from e_commerce.models import Address


# Create your views here.
def register(request):
    if request.method == 'POST':
        if request.POST.get('username') and request.POST.get('password'):
            savefullname = Fullname()
            savefullname.firstname = request.POST.get('firstName')
            savefullname.lastname = request.POST.get('lastName')
            savefullname.save()
            new_name = Fullname.objects.filter(firstname=savefullname.firstname, lastname=savefullname.lastname)
            FullnameID = new_name.get()

            saveuser = Account()
            saveuser.username = request.POST.get('username')
            saveuser.password = request.POST.get('password')
            saveuser.role = 1
            saveuser.save()

            new_user = Account.objects.filter(username=saveuser.username, password=saveuser.password)
            userid = new_user.get()

            saveaddress = Address()
            saveaddress.city = request.POST.get('city')
            saveaddress.district = request.POST.get('district')
            saveaddress.ward = request.POST.get('ward')
            saveaddress.description = request.POST.get('description')
            saveaddress.save()

            newaddress = Address.objects.filter(city=saveaddress.city, district=saveaddress.district,
                                                description=saveaddress.description)
            addressid = newaddress.get()

            savecustomer = Customer()
            savecustomer.accountid = userid
            savecustomer.fullnameid = FullnameID
            savecustomer.addressid = addressid
            savecustomer.email = request.POST.get('email')
            savecustomer.tel = request.POST.get('tel')
            savecustomer.save()

            messages.success(request, "Success")
            return render(request, "register.html")

    else:
        return render(request, "register.html")


def login(request):
    if request.method == 'POST':
        get_user = Account.objects.filter(username=request.POST.get('username'),
                                          password=request.POST.get('password')).count()
        user = Account.objects.filter(username=request.POST.get('username'), password=request.POST.get('password'))
        if get_user == 0:
            messages.success(request, "Fail")
        else:
            user_role = user.get().role
            if user_role == "0":
                request.session['user_id'] = user.get().id
                return redirect('../employee')
            else:
                return redirect('../')
        return render(request, "login.html")
    else:
        return render(request, "login.html")


def homepage(request):
    return render(request, "homepage.html")


def admin(request):
    user_id = request.session.get('user_id')
    get_current_user = Account.objects.filter(id=user_id)
    current_user = get_current_user.get()
    get_employee = Employee.objects.filter(accountid=current_user)
    employee = get_employee.get()
    return render(request, "admin/admin.html", {'employee': employee})


def product(request):
    return render(request, "admin/product.html")


def add_product(request):
    return render(request, "admin/add_product.html")