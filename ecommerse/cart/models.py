from django.db import models
from shop.models import product
from django.contrib.auth.models import User

class cart(models.Model):
    product=models.ForeignKey(product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    date_added=models.DateTimeField(auto_now_add=True)

    def subtotal(self):
        return self.quantity*self.product.price

    def __str__(self):
        return self.product.name


class order(models.Model):
    product=models.ForeignKey(product, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    no_of_items=models.IntegerField()
    phone=models.BigIntegerField()
    address=models.TextField()
    ordered_date=models.DateTimeField(auto_now_add=True)
    order_status=models.CharField(max_length=30,default="pending")
    delivery_status=models.CharField(max_length=30,default="pending")

    def __str__(self):
        return self.user.username


class account(models.Model):
    acc_num=models.BigIntegerField()
    acc_type=models.CharField(max_length=20)
    amount=models.IntegerField()

    def __str__(self):
        return str(self.acc_num)

