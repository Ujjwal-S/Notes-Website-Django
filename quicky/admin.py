from django.contrib import admin
from .models import *


admin.site.register(User)
admin.site.register(Referral)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Subscriber)