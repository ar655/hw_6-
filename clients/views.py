from django.shortcuts import render

from .models import Client , Order
from .forms import OrderForm
from django.views.generic import DetailView,ListView
from django.views import View
from django.views.generic.edit import UpdateView

# def clients_list(request):
#     context = {}
#     context['clients_lisst'] = Client.objects.all()
#     return render(request,'clients.html',context)

class ClientListView(ListView):
    model = Client
    template_name = 'clients.html'



class ClientInfoView(DetailView):
    model = Client
    template_name = 'client_info.html'



class DataUpdate(UpdateView):
    model = Client
    fields = ['name','address','active','bottles_ordered','photo']
    template_name = 'client_update.html'



def orders_list(request):
    context = {}
    context['orders_lisst'] = Order.objects.all()
    return render(request,'orders.html',context)


# def orders_inffo(request,id):
#     context = {
#         'order': Order.objects.get(id=id)
#
#     }
#     return render(request,'orders_info.html',context)


class OrderInfoView(DetailView):
    model = Order
    template_name = 'orders_info.html'




class MyView(View):
    def get(self,request):
        return render(request,"about.html")





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