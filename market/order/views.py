from django.shortcuts import render, redirect
from django.http import HttpResponse
from order.models import Order, OrderProduct
from user.models import Customer
from django.shortcuts import get_object_or_404

def listOrders(request):
    
    customerToShow = Customer.objects.get(user=request.user)
    orders = Order.objects.filter(customer=customerToShow)
    
    
    context = {
        'orders': orders ,
    }

    return render(request, 'order/orderList.html', context)



def showDetail(request,order_id:int):
    
    order = get_object_or_404(Order, pk = order_id)
    order_products = OrderProduct.objects.filter(order__id=order_id).select_related('product')

    
    context = {
        'order': order,
        'order_products': order_products,
    }
    
    return render(request, 'order/orderDetail.html', context)