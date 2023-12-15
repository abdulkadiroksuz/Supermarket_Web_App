from django.shortcuts import render
from order.models import Order
from user.models import Customer


def listOrders(request):
    
    customerToShow = Customer.objects.get(user=request.user)
    orders = Order.objects.filter(customer=customerToShow)
    
    
    context = {
        'orders': orders ,
    }

    return render(request, 'order/orderList.html', context)