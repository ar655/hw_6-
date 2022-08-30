from django.shortcuts import render

from .models import Client , Order
from .forms import OrderForm



def clients_list(request):
    context = {}
    context['clients_lisst'] = Client.objects.all()
    return render(request,'clients.html',context)


def orders_list(request):
    context = {}
    context['orders_lisst'] = Order.objects.all()
    return render(request,'orders.html',context)


def orders_inffo(request,id):
    context = {
        'order': Order.objects.get(id=id)

    }
    return render(request,'orders_info.html',context)


def orders_update(request,id):
    context = {}
    order_data = Order.objects.get(id=id)
    if request.method == 'POST':
        form = OrderForm(request.POST,instance=order_data)
        if form.is_valid():
            order_data = form.save()
    context['form'] = OrderForm(instance=order_data)
    return render(request,'orders_update.html',context)





def about(request):
    return render(request,'about.html')