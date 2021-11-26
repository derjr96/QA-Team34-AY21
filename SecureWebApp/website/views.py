from django.shortcuts import render, redirect
from .models import Product, Order, OrderItem, ShippingAddress
from django.contrib.auth.decorators import login_required
from .decorator import seller_only, customer_only
from .forms import ProductForm
from django.http import JsonResponse
import json
import datetime
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

# HOME/MainPage
def home(request):
    products = Product.objects.all()

    context = {
        'catalog': products,
        'title': 'Home',
        'item_titles': Product.objects.values('title').distinct()
    }
    return render(request, 'website/home.html', context)


# Add to cart
@csrf_exempt
@login_required
@customer_only
def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action:', action)
    print('productId:', productId)

    user = request.user
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(user=user, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order_ID=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
        print('orderItem:', orderItem.quantity)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity < 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)


@csrf_exempt
@login_required
@customer_only
def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    if request.user.is_authenticated:
        user = request.user
        order, created = Order.objects.get_or_create(user=user, complete=False)
        total = float(data['form']['total'])
        order.transaction_ID = transaction_id

        if total == order.get_cart_total:
            order.complete = True
        order.save()
        if order.shipping is True:
            ShippingAddress.objects.create(
                profile=user,
                order_ID=order,
                address=data['shipping']['address'],
                city=data['shipping']['city'],
                state=data['shipping']['state'],
                zipcode=data['shipping']['zipcode'],
            )
    else:
        print('User is not logged in')

    return JsonResponse('Payment Complete', safe=False)


# AboutPage
def about(request):
    context = {
        'title': 'About'
    }
    return render(request, 'website/about.html', context)


# CartPage
@login_required
@customer_only
def cart(request):
    if request.user.is_authenticated:
        user = request.user
        order, created = Order.objects.get_or_create(user=user, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}

    context = {
        'title': 'Cart',
        'items': items,
        'order': order
    }
    return render(request, 'website/cart.html', context)


# checkout Page
@login_required
@customer_only
def checkout(request):
    if request.user.is_authenticated:
        user = request.user
        order, created = Order.objects.get_or_create(user=user, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}

    context = {
        'title': 'Checkout',
        'items': items,
        'order': order
    }
    return render(request, 'website/checkout.html', context)


@login_required
@seller_only
def seller(request):
    context = {
        'title': 'Seller',
        'catalog': Product.objects.all(),
    }

    return render(request, 'website/seller.html', context)


@login_required
@seller_only
def createProduct(request):
    form = ProductForm
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.cleaned_data.get('itemname')
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            messages.success(request, f'Product {product} created')
            return redirect('/')

    context = {
        'title': 'Seller Order',
        'form': form,
        'catalog': Product.objects.all(),
    }
    return render(request, 'website/createorder.html', context)


@login_required
@seller_only
def updateProduct(request, pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'title': 'Seller Order',
        'form': form,
        'catalog': Product.objects.all(),
    }
    return render(request, 'website/createorder.html', context)


@login_required
@seller_only
def deleteProduct(request, pk):
    product = Product.objects.get(id=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('rock-seller')

    context = {'item': product}
    return render(request, 'website/deleteproduct.html', context)
