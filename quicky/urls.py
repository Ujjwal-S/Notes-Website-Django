from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.home, name="home"),
    path('profile/', views.profile, name="profile"),

    path('cart/', views.cart, name="cart"),
    path('my_cart_info/', views.my_cart_info, name="my_cart_info"),
    path('remove_item/', views.remove_item, name="remove_item"),
    path('checkout/', views.checkout, name="checkout"),
    # path('process_order/', views.process_order, name="process_order"),

    path('checkemail/<str:email>', views.emailExists, name="checkEmailExists"),
    path('addsubscriber/<str:email>', views.addSubscriber, name="addSubscriber"),

    path('verify_razorpay_payment/', views.verify_razorpay_payment, name="verify_razorpay_payment"),

    path('learn_more_about_points/', TemplateView.as_view(template_name="quicky/learn_more.html"))
]