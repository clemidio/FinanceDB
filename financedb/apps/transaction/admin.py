from django.contrib import admin
from .models import Transaction


# Register your models here.
# admin.site.register(Transaction)
@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'asset',
        'date',
        'amount',
        'price',
        'commission',
        'nota_id',
        'obs',
        'last_update',
    )
    search_fields = ('asset',)
    list_filter = ('date', "asset",)
