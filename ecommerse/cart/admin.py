from django.contrib import admin
from django.http import Httpresponse
from cart.models import cart,order,account

admin.site.register(cart)
admin.site.register(order)
admin.site.register(account)

