from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from shop.models import product
from cart.models import cart,account,order
from django.http import HttpResponse
@login_required
# For displaying cart for the current user
def cart_view(request):
    u=request.user
    total=0
    c=cart.objects.filter(user=u)
# To find the total amount
    for i in c:
        total=total+i.quantity*i.product.price

    return render(request,'cart.html',{'c':c,'total':total})


@login_required
# for adding a particular product to the cart table
def addtocart(request,p):
    p=product.objects.get(id=p)
    u=request.user
    try:
        Cart=cart.objects.get(user=u,product=p)
        if(p.stock>0):
            Cart.quantity+=1
            Cart.save()
            p.stock-=1
            p.save()
    except:
        if(p.stock>0):
            Cart=cart.objects.create(user=u,product=p,quantity=1)
            Cart.save()
            p.stock-=1
            p.save()

    return cart_view(request)


def cartremove(request,p):
    p = product.objects.get(id=p)
    u = request.user
    try:
        Cart = cart.objects.get(user=u, product=p)
        if (Cart.quantity>1):
            Cart.quantity -= 1
            Cart.save()
            p.stock += 1
            p.save()

        else:
            Cart.delete()
            p.stock+=1
            p.save()
    except:
        pass
    return cart_view(request)

def fullremove(request,p):
    p = product.objects.get(id=p)
    u = request.user
    try:
        Cart=cart.objects.get(user=u, product=p)
        Cart.delete()
        p.stock+=cart.quantity
        p.save()

    except:
        pass

    return cart_view(request)

@login_required
def orderform(request):
    if(request.method=="POST"):
        p=request.POST['p']
        a=request.POST['a']
        n=request.POST['n']

        u=request.user
        c=cart.objects.filter(user=u)

        total=0
        for i in c:
            total=total+i.quantity*i.product.price

        try:
            acc=account.objects.get(acc_num=n)
            if(acc.amount>=total):
                print(acc.amount)
                acc.amount=acc.amount-total
                print(acc.amount)
                acc.save()
                for i in c:
                    print("hello")
                    o=order.objects.create(user=u,product=i.product,address=a,phone=p,no_of_items=i.quantity,order_status="paid")
                    print("hello")
                    o.save()
                c.delete()
                msg="Your order placed successfully"
                return render(request,'orderdetail.html',{'message':msg})
            else:
                msg="insufficient amount,please check your balance."
                return render(request,'orderdetail.html',{'message':msg})


        except:
            pass

    return render(request,'orderform.html')


def orderview(request):
    u=request.user
    o=order.objects.filter(user=u)

    return render(request,'orderview.html',{'o':o,'u':u.username})