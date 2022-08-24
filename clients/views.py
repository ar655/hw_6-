from django.shortcuts import render

from .models import Client



def clients_list(request):
    context = {}
    context['clients_lisst'] = Client.objects.all()
    return render(request,'clients.html',context)


def about(request):
    return render(request,'about.html')