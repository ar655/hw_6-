from django.contrib import admin

from .models import Client,Order


class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = ['name', 'contacts', 'ordered_at', 'finished']
    list_editable = ['contacts', 'finished']
    fields = ['name', 'contacts', 'ordered_at', 'updated_at', 'discription', 'finished']
    readonly_fields = ['ordered_at', 'updated_at']


admin.site.register(Order, OrderAdmin)




admin.site.register(Client)
