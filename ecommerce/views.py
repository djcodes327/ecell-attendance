from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Product, Category, Customer, Orders
from django.contrib.auth.hashers import make_password, check_password
from .serializers import ProductSerializer


# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


def index(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    email = request.session.get('customer_email')
    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'index.html', context)


def about(request):
    return None


def collection(request):
    if request.method == "GET":
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        products_collection = None
        categories_collection = Category.objects.all()
        categoryfilter = request.GET.get('category')
        if categoryfilter:
            products_collection = Product.objects.filter(categories=categoryfilter, )
        else:
            products_collection = Product.objects.all()

        context = {
            'products': products_collection,
            'categories': categories_collection
        }
        return render(request, 'collection.html', context)

    else:
        product = request.POST.get('product')
        cart = request.session.get('cart')
        remove = request.POST.get('remove')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
        request.session['cart'] = cart

        return redirect('collection')


def signup(request):
    if request.method == "POST":
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone')
        password = request.POST.get('password')
        password = make_password(password)

        email_exists = None
        if Customer.objects.filter(email=email, ):
            email_exists = True
        else:
            email_exists = False
        value = {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "phone_number": phone_number,
        }

        error_message = None

        if not first_name:
            error_message = "First Name is Required!!!"
        elif not last_name:
            error_message = "Last Name is Required!!!"
        elif email_exists:
            error_message = "Email is Already Registered"
        elif not email:
            error_message = "E-Mail is Required!!!"
        elif not phone_number:
            error_message = "Phone Number is Required!!!"
        elif len(phone_number) <= 9:
            error_message = "Please Enter a Valid Phone Number"
        elif not password:
            error_message = "Password is Required!!!"

        if not error_message:
            Customer.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone_number=phone_number,
                password=password,
            )
            messages.success(request, "New User Registered Successfully")
            return redirect('signup')
        else:
            context = {
                "error_message": error_message,
                "values": value
            }
            return render(request, 'signup.html', context)

    else:
        return render(request, 'signup.html', {})


def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.objects.get(email=email)
        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer'] = customer
                request.session['customer_id'] = customer.id
                request.session['customer_email'] = customer.email
                return redirect('index_shop')
            else:
                error_message = "Email/Password is Wrong !!! Plzz Try Again"

        else:
            error_message = "Email/Password is Wrong !!! Plzz Try Again"
        context = {
            "error_message": error_message
        }

        return render(request, 'login.html', context)
    else:
        return render(request, 'login.html', {})


def logout(request):
    request.session.clear()
    return redirect('login')


def cart(request):
    error_message = None
    products = ""
    cart = list(request.session.get('cart').keys())
    status_cart = bool(cart)
    if not status_cart:
        error_message = "Cart is Empty"
    else:
        products = Product.objects.filter(id__in=cart)
    context = {
        'products': products,
        'error_message': error_message
    }
    return render(request, 'cart.html', context)


def checkout(request):
    if request.method == "POST":
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer_id')
        cart_keys = list(request.session.get('cart').keys())
        cart = request.session.get('cart')
        products = Product.objects.filter(id__in=cart_keys)

        for product in products:
            Orders.objects.create(
                customer=Customer(id=customer),
                address=address,
                phone=phone,
                price=product.price,
                product=product,
                quantity=cart.get(str(product.id))
            )
            request.session['cart'] = {}

        return redirect('cart')


def orders(request):
    customer = request.session.get('customer_id')
    customer_order = Orders.objects.filter(customer=customer)
    print(customer_order)

    return render(request, 'orders.html')
