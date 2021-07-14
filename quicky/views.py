from typing import final
from django.shortcuts import render, redirect
from . models import *
from notes.models import MyNote, Note
from django.http import HttpResponse
import json
import time
from django.views.decorators.csrf import csrf_exempt
# from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
import uuid
from django.contrib.sites.models import Site
import razorpay



def home(request):
    return render(request, 'quicky/home.html')


def emailExists(request, email):
    
    response = HttpResponse(json.dumps({'emailExists': User.objects.filter(email=email).exists()}))
    
    return response


def addSubscriber(request, email):

    if (Subscriber.objects.filter(email=email).exists()):
        return HttpResponse(json.dumps({'added': False}))

    subscriber = Subscriber.objects.create(email=email)
    subscriber.save()

    return HttpResponse(json.dumps({'added': True}))



def cart(request):
    if request.user.is_authenticated :
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)

        order_items = OrderItem.objects.filter(order=order)

        context = {'order_items': order_items}

        return render(request, 'quicky/cart.html', context)

    
    return HttpResponse("<p style='text-align: center; margin-top: 40px;'>Login to Continue</p>")



@csrf_exempt
def my_cart_info(request):
    data = json.loads(request.body)

    notes_id = data['notes-id']
    note_name = Note.objects.get(id=notes_id)

    order, created = Order.objects.get_or_create(customer=request.user, complete=False)

    if OrderItem.objects.filter(note_name=note_name, order=order).exists():
        added = False

    else:
        OrderItem.objects.create(note_name=note_name, order=order)
        added = True

    latest_count = OrderItem.objects.filter(order=order).count()
    print("\n"*10)
    print(latest_count)
    print("\n"*10)

    return HttpResponse(json.dumps({'added': added, 'latest_count': latest_count}))
    



@csrf_exempt
def remove_item(request):
    data = json.loads(request.body)

    remove_order_item_id = data['remove_order_item_id']

    OrderItem.objects.get(id=remove_order_item_id).delete()

    order = Order.objects.get(customer=request.user, complete=False)
    latest_count = OrderItem.objects.filter(order=order).count()

    return HttpResponse(json.dumps({'removed': True, 'latest_count': latest_count}))

def profile(request):
    
    if request.method == "POST":
        user = request.user
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password1']
        password2 = request.POST['password2']
        

        if first_name != user.first_name:
            user.first_name = first_name
        if last_name != user.last_name:
            user.last_name = first_name
        if password != '' and password == password2 and len(password) >= 8:
            user.set_password(password)

        user.save()
        
        if password != '' and password == password2 and len(password) >= 8:
            upbhohgta = authenticate(username=user.username, password=password)

            if upbhohgta is not None:
                login(request, upbhohgta)
                return redirect('/profile')
            
            return redirect('/')
        else:
            return redirect('/profile')
    
    context = {}
    return render(request, 'quicky/profile.html', context)


def checkout(request):
    if request.user.is_authenticated :
        customer = request.user
        my_order, created = Order.objects.get_or_create(customer=customer, complete=False)
        orderItems = OrderItem.objects.filter(order=my_order)

        checkout_total = sum([x.note_name.price for x in orderItems])

        # my_order IS USERS CART
        # order AND order.id IS RAZORPAY

        razorpay_client = razorpay.Client(auth=('rzp_test_G0OCZoTqqEwDLs', 'wMglOKwqsrYbfl6DncLeuwiA'))
        data = {
            'amount': 100,
            'currency': 'INR',
            'receipt': 'test receipt',
            'receipt': str(my_order.recipt),
            'payment_capture': 1
        }

        order = razorpay_client.order.create(data)
        order_id = order['id']

        my_order.order_id = order_id

        context = {
            'order_id': order_id,
            'cart_order_id': my_order.id,
            'orderItems': orderItems,
            'orderItemsCount': orderItems.count(),
            'checkout_total': checkout_total
        }        

        return render(request, 'quicky/checkout.html', context)

    return HttpResponse("<p style='text-align: center; margin-top: 40px;'>Login to Continue</p>")



# @csrf_exempt
# def check_order(request):
#     # info from server
#     order, created = Order.objects.get_or_create(customer=request.user, complete=False)
#     orderItems = OrderItem.objects.filter(order=order)
#     s_orderItemsId = []  # list of orderItems id to be later compared with the user sent info
#     for i in orderItems:
#         s_orderItemsId.append(str(i.id))

#     checkout_total = sum([x.note_name.price for x in orderItems])


#     # info from user
#     data = json.loads(request.body)


#     # checking if bot server and user info match

#     if s_orderItemsId == data['list_of_orderItemsId']:

#         if str(checkout_total) == data['final_price'] or str(checkout_total - request.user.points) == data['final_price']:

#             return HttpResponse(json.dumps({'correct_data': True, 'final_price':data['final_price']}))

#     return HttpResponse(json.dumps({'correct_data': False}))


# @csrf_exempt
# def process_order(request):

#     order, created = Order.objects.get_or_create(customer=request.user, complete=False)
#     orderItems = OrderItem.objects.filter(order=order)
    
#     data = json.loads(request.body)
#     final_price = data['final_price']

#     razorpay_client = razorpay.Client(auth=('rzp_test_G0OCZoTqqEwDLs', 'wMglOKwqsrYbfl6DncLeuwiA'))
    
#     data = {
#         'amount': int(final_price) * 100,
#         'currency': 'INR',
#         'receipt': 'test receipt',
#         'payment_capture': 1
#     }

#     r_order = razorpay_client.order.create(data)
#     r_order_id = r_order['id']

#     context = {
#         'r_order':r_order, 
#         'r_order_id': r_order_id,
#         'u_order_id': order.id
#         }

#     return render(request, 'quicky/pay_amount.html', context)

#     # order.complete = True
#     # order.save()
#     # for order_item_id in s_orderItemsId:
#     #     MyNote.objects.create(customer=request.user, note=Note.objects.get(id=OrderItem.objects.get(id=int(order_item_id)).note_name.id))