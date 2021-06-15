from django.shortcuts import redirect, render
from django.contrib import messages
from e_commerce.models import Account, Employee, Customer, Fullname, Address, Product
from e_commerce.models import Cart, Item


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
                request.session['user_id'] = user.get().id
                return redirect('../homepage')
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
    all_product = Product.objects.all()
    return render(request, "admin/product.html", {'products': all_product})


def add_product(request):
    if request.method == 'POST':
        if request.POST.get('product_name') and request.POST.get('quantity') and request.POST.get('image_url') and request.POST.get('price'):
            saveproduct = Product()
            saveproduct.product_name = request.POST.get('product_name')
            saveproduct.quantity = request.POST.get('quantity')
            saveproduct.product_type = request.POST.get('product_type')
            saveproduct.price = request.POST.get('price')
            saveproduct.image = request.POST.get('image_url')
            if(request.POST.get('publicCheck') =='on'):
                saveproduct.public = 1
            else:
                saveproduct.public = 0
            saveproduct.save()
            messages.success(request, "Success")
            return render(request, "admin/add_product.html")

    else:
        return render(request, "admin/add_product.html")


def customer(request):
    all_product = Product.objects.filter(public=1)
    if(all_product.count()!=0):
        return render(request, "customer/index.html", {'products': all_product})
    else:
        return render(request, "customer/index.html")

def addtocart(request,id):
    #get Item
    get_product = Product.objects.filter(id=id)
    product = get_product.get()
    #get Customer
    get_account = Account.objects.filter(id=request.session['user_id'])
    account = get_account.get()
    get_customer = Customer.objects.filter(accountid = account)
    current_customer = get_customer.get()
    get_cart = Cart.objects.filter(status="onhold",customerid = current_customer).count()
    if(get_cart==0):
        savecart = Cart()
        savecart.price = product.price
        savecart.status="onhold"
        savecart.customerid = current_customer
        savecart.save()
        new_cart = Cart.objects.filter(status="onhold", customerid = current_customer).get()
        saveitem = Item()
        saveitem.quantity = 1
        saveitem.price = new_cart.price
        saveitem.productid = product
        saveitem.cartid =new_cart
        saveitem.save()
        messages.success(request, "Success")
        return redirect('../homepage')
    else:
        current_cart = Cart.objects.filter(status="onhold", customerid = current_customer).get()
        current_cart.price = product.price + current_cart.price
        current_cart.status="onhold"
        current_cart.customerid = current_customer
        current_cart.save()
        new_cart = Cart.objects.filter(status="onhold", customerid = current_customer).get()
        saveitem = Item()
        saveitem.quantity = 1
        saveitem.price = product.price
        saveitem.productid = product
        saveitem.cartid =new_cart
        saveitem.save()
        messages.success(request, "Success")
        return redirect('../homepage')
