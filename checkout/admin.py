from django.contrib import admin
from .models import Order, LineItem


class LineItemAdmin(admin.TabularInline):
    model = LineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (LineItemAdmin,)
    readonly_fields = ('order_number', 'date',
                       'order_total', 'grand_total')

    fields = ('order_number', 'date',
              'order_total', 'grand_total', 'email')
    
    list_display = ('email', 'order_number', 'date', 'grand_total')

    ordering = ('-date',)

admin.site.register(Order, OrderAdmin)