from django.shortcuts import redirect, render
from django.contrib import messages
from e_commerce.models import Account, Employee, Customer, Fullname, Address, Product, Rating, Ratingprocess
from e_commerce.models import Cart, Item, Payment, Shipment, Order, Orderprocess, Productrating


# Create your views here.
def register(request):
    if request.method == 'POST':
        if request.POST.get('username') and request.POST.get('password'):
            savefullname = Fullname()
            savefullname.firstname = request.POST.get('firstName')
            savefullname.lastname = request.POST.get('lastName')
            savefullname.save()

            saveuser = Account()
            saveuser.username = request.POST.get('username')
            saveuser.password = request.POST.get('password')
            saveuser.role = 1
            saveuser.save()

            saveaddress = Address()
            saveaddress.city = request.POST.get('city')
            saveaddress.district = request.POST.get('district')
            saveaddress.ward = request.POST.get('ward')
            saveaddress.description = request.POST.get('description')
            saveaddress.save()

            savecustomer = Customer()
            savecustomer.accountid = saveuser
            savecustomer.fullnameid = savefullname
            savecustomer.addressid = saveaddress
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
        user = Account.objects.filter(username=request.POST.get(
            'username'), password=request.POST.get('password'))
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
    all_product = Product.objects.filter(public=1)
    return render(request, "homepage.html", {'products': all_product})

# Employee role


def admin(request):
    if request.session.get('user_id') is None:
        return redirect('../login')
    else:
        user_id = request.session.get('user_id')
        get_current_user = Account.objects.filter(id=user_id)
        current_user = get_current_user.get()
        get_employee = Employee.objects.filter(accountid=current_user)
        employee = get_employee.get()
        return render(request, "admin/admin.html", {'employee': employee})


def product(request):
    if request.session.get('user_id') is None:
        return redirect('../login')
    all_product = Product.objects.all()
    return render(request, "admin/product.html", {'products': all_product})


def add_product(request):
    if request.session.get('user_id') is None:
        return redirect('../login')
    else:
        if request.method == 'POST':
            if request.POST.get('product_name') and request.POST.get('quantity') and request.POST.get('image_url') and request.POST.get('price'):
                saveproduct = Product()
                saveproduct.product_name = request.POST.get('product_name')
                saveproduct.quantity = request.POST.get('quantity')
                saveproduct.product_type = request.POST.get('product_type')
                saveproduct.description = request.POST.get('description')
                saveproduct.price = request.POST.get('price')
                saveproduct.image = request.POST.get('image_url')
                if(request.POST.get('publicCheck') == 'on'):
                    saveproduct.public = 1
                else:
                    saveproduct.public = 0
                saveproduct.save()
                messages.success(request, "Success")
                return render(request, "admin/add_product.html")

        else:
            return render(request, "admin/add_product.html")


def admin_order(request):
    if request.session.get('user_id') is None:
        return redirect('../login')
    all_order = Order.objects.all()
    return render(request, "admin/adminorder.html", {'orders': all_order})


def orderprocess(request, id):
    if request.session.get('user_id') is None:
        return redirect('../login')
    get_order = Order.objects.filter(id=id).get()
    get_cart = get_order.cartid
    get_items = Item.objects.filter(cartid=get_cart)

    user_id = request.session.get('user_id')
    get_current_user = Account.objects.filter(id=user_id)
    current_user = get_current_user.get()
    get_employee = Employee.objects.filter(accountid=current_user)
    employee = get_employee.get()

    get_process = Orderprocess.objects.filter(
        employeeid=employee, orderid=get_order)

    if(get_process.count() == 0):
        if request.method == 'POST':
            saveprocess = Orderprocess()
            saveprocess.employeeid = employee
            saveprocess.orderid = get_order
            saveprocess.save()

            get_cart.status = request.POST.get('order_status')
            get_cart.save()
            get_order.status = request.POST.get('order_status')
            get_order.save()
            return redirect('../order')
        else:
            return render(request, "admin/orderprocess.html", {'items': get_items, 'order': get_order, 'employee': employee})
    else:
        get_my_process = Orderprocess.objects.filter(
            employeeid=employee, orderid=get_order)
        if get_my_process.count() != 0:
            if request.method == 'POST':
                saveprocess = Orderprocess()
                saveprocess.employeeid = employee
                saveprocess.orderid = get_order
                saveprocess.save()

                get_cart.status = request.POST.get('order_status')
                get_cart.save()
                get_order.status = request.POST.get('order_status')
                get_order.save()
                return redirect('../order')
            else:
                return render(request, "admin/orderprocess.html", {'items': get_items, 'order': get_order, 'employee': employee})
        else:
            return redirect('../order')


def editproduct(request,id):
    if request.session.get('user_id') is None:
        return redirect('../login')
    else:
        get_product = Product.objects.filter(id=id).get()
        if request.method == 'POST':
            if request.POST.get('product_name') and request.POST.get('quantity') and request.POST.get('image_url') and request.POST.get('price'):
                get_product.product_name = request.POST.get('product_name')
                get_product.quantity = request.POST.get('quantity')
                get_product.product_type = request.POST.get('product_type')
                get_product.description = request.POST.get('description')
                get_product.price = request.POST.get('price')
                get_product.image = request.POST.get('image_url')
                if(request.POST.get('publicCheck') == 'on'):
                    get_product.public = 1
                else:
                    get_product.public = 0
                get_product.save()
                messages.success(request, "Success")
                return redirect('../product')
        else:
            return render(request, "admin/editproduct.html", {'product': get_product})


def adminrating(request):
    if request.session.get('user_id') is None:
        return redirect('../login')
    get_product_ratings = Productrating.objects.all()
    return render(request, "admin/productrating.html", {'ratings': get_product_ratings})


def ratingprocess(request,id):
    if request.session.get('user_id') is None:
        return redirect('../login')
    get_account = Account.objects.filter(id=request.session['user_id'])
    account = get_account.get()
    if(account.role != "0"):
        return redirect('../login')  
    get_employee = Employee.objects.filter(accountid = account)
    employee = get_employee.get()  
    get_product_rating = Productrating.objects.filter(id = id).get()    
    if request.method == 'POST':
        saveratingprocess = Ratingprocess()
        saveratingprocess.employeeid = employee
        saveratingprocess.ratingid = get_product_rating.ratingid
        saveratingprocess.feedback = request.POST.get("feedback")
        saveratingprocess.save()
        return render(request, "admin/ratingprocess.html", {'productrating': get_product_rating, "ratingprocess": saveratingprocess})
    else:
        saveratingprocess = Ratingprocess.objects.filter(ratingid  = get_product_rating.ratingid)
        if saveratingprocess.count() != 0:
            process = saveratingprocess.get()
            return render(request, "admin/ratingprocess.html", {'productrating': get_product_rating,  "ratingprocess": process})
        else:
            return render(request, "admin/ratingprocess.html", {'productrating': get_product_rating})

# Customer role
def customer(request):
    all_product = Product.objects.filter(public=1)
    return render(request, "customer/index.html", {'products': all_product})


def addtocart(request, id):
    if request.session.get('user_id') is None:
        return redirect('../login')
    else:
        # get Item
        get_product = Product.objects.filter(id=id)
        product = get_product.get()
        # get Customer
        get_account = Account.objects.filter(id=request.session['user_id'])
        account = get_account.get()
        get_customer = Customer.objects.filter(accountid=account)
        current_customer = get_customer.get()
        get_cart = Cart.objects.filter(
            status="onhold", customerid=current_customer).count()
        if(get_cart == 0):
            savecart = Cart()
            savecart.price = product.price
            savecart.status = "onhold"
            savecart.customerid = current_customer
            savecart.save()
            new_cart = Cart.objects.filter(
                status="onhold", customerid=current_customer).get()
            saveitem = Item()
            saveitem.quantity = 1
            saveitem.price = new_cart.price
            saveitem.productid = product
            saveitem.cartid = new_cart
            saveitem.save()
            messages.success(request, "Success")
            return redirect('../cart')
        else:
            current_cart = Cart.objects.filter(
                status="onhold", customerid=current_customer).get()
            current_cart.price = product.price + current_cart.price
            current_cart.status = "onhold"
            current_cart.customerid = current_customer
            current_cart.save()
            new_cart = Cart.objects.filter(
                status="onhold", customerid=current_customer).get()
            saveitem = Item()
            saveitem.quantity = 1
            saveitem.price = product.price
            saveitem.productid = product
            saveitem.cartid = new_cart
            saveitem.save()
            messages.success(request, "Success")
            return redirect('../cart')


def cart(request):
    if request.session.get('user_id') is None:
        return redirect('../login')
    else:
        get_account = Account.objects.filter(id=request.session['user_id'])
        account = get_account.get()
        if account.role == '1':
            get_customer = Customer.objects.filter(accountid=account)
            current_customer = get_customer.get()
            get_cart = Cart.objects.filter(
                status="onhold", customerid=current_customer)
            if(get_cart.count() != 0):
                get_items = Item.objects.filter(cartid=get_cart.get())
                return render(request, "customer/cart.html", {'items': get_items, 'mycart': get_cart.get()})
            else:
                return render(request, "customer/cart.html")
        else:
            return redirect('../login')


def confirm(request):
    if request.session.get('user_id') is None:
        return redirect('../login')
    else:
        get_account = Account.objects.filter(id=request.session['user_id'])
        account = get_account.get()
        get_customer = Customer.objects.filter(accountid=account)
        current_customer = get_customer.get()
        get_cart = Cart.objects.filter(
            status="onhold", customerid=current_customer)
        if(get_cart.count() == 0):
            return redirect("../homepage")
        if request.method == 'POST':
            my_cart = get_cart.get()
            # save payment
            savepayment = Payment()
            if request.POST.get('checkPayment') == "pay1":
                savepayment.payment_type = "thanh toán bằng thẻ"
            else:
                savepayment.payment_type = "thanh toán khi nhận hàng"
            savepayment.price = my_cart.price
            savepayment.save()

            saveshipment = Shipment()
            if request.POST.get('checkShipment') == "ship1":
                saveshipment.shipment_type = "giao hàng nhanh"
                saveshipment.fee = 25000
            else:
                saveshipment.shipment_type = "giao hàng tiêu chuẩn"
                saveshipment.fee = 0
            saveshipment.addressid = current_customer.addressid
            saveshipment.save()

            saveorder = Order()
            saveorder.price = saveshipment.fee + my_cart.price
            saveorder.status = "chờ xác nhận"
            saveorder.cartid = my_cart
            saveorder.paymentid = savepayment
            saveorder.shipmentid = saveshipment
            saveorder.save()
            # update cart
            my_cart.status = "wait"
            my_cart.save()
            get_items = Item.objects.filter(cartid=my_cart)
            return redirect("../order")
        else:
            get_items = Item.objects.filter(cartid=get_cart.get())
            return render(request, "customer/confirm.html", {'items': get_items, 'mycart': get_cart.get()})


def order(request):
    if request.session.get('user_id') is None:
        return redirect('../login')
    get_account = Account.objects.filter(id=request.session['user_id'])
    account = get_account.get()
    get_customer = Customer.objects.filter(accountid=account)
    current_customer = get_customer.get()
    get_carts = Cart.objects.filter(customerid=current_customer)
    list_order = []
    for cart in get_carts:
        if(cart.status != "onhold"):
            get_order = Order.objects.filter(cartid=cart).get()
            list_order.append(get_order)
    return render(request, "customer/order.html", {'orders': list_order})


def orderdetail(request, id):
    if request.session.get('user_id') is None:
        return redirect('../login')
    get_order = Order.objects.filter(id=id).get()
    get_cart = get_order.cartid
    get_items = Item.objects.filter(cartid=get_cart)
    return render(request, "customer/orderdetail.html", {'items': get_items, 'order': get_order})


def rating(request, id):
    if request.session.get('user_id') is None:
        return redirect('../login')
    get_account = Account.objects.filter(id=request.session['user_id'])
    account = get_account.get()
    get_customer = Customer.objects.filter(accountid=account)
    current_customer = get_customer.get()
    get_order = Order.objects.filter(id=id).get()
    get_cart = get_order.cartid
    get_items = Item.objects.filter(cartid=get_cart)
    if get_order.status == "Đã hoàn thành":
        if request.method == 'POST':
            for item in get_items:
                comment = str(item.id)+'comment'
                rating = str(item.id)+'rating'
                # Rating
                saverating = Rating()
                saverating.star = request.POST.get(rating)
                saverating.comment = request.POST.get(comment)
                saverating.itemid = item
                saverating.customerid = current_customer
                # save
                saverating.save()
                # Productrating
                savepr = Productrating()
                savepr.ratingid = saverating
                savepr.productid = item.productid
                savepr.save()
            return redirect('../homepage')
        else:
            return render(request, "customer/rating.html", {'items': get_items, 'order': get_order})
    else:
        return redirect('../order')


def productdetail(request, id):
    get_product = Product.objects.filter(id=id).get()
    get_product_ratings = Productrating.objects.filter(productid=get_product)
    sumrate = 0
    list_ratings = []
    for rate in get_product_ratings:
        get_rate = rate.ratingid
        list_ratings.append(get_rate)
        sumrate += get_rate.star
    averageRating = 0
    coutrating = 0
    if len(list_ratings) != 0:
        averageRating = sumrate/len(list_ratings) 
        coutrating = len(list_ratings) 
    return render(request, "productdetail.html", {'product': get_product, 'ratings': list_ratings, 'averageStar': averageRating, 'count': coutrating})
