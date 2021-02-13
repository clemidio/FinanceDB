from django.contrib import admin
from .models import Nota

# Register your models here.
#admin.site.register(Nota)
@admin.register(Nota)
class NotaAdmin(admin.ModelAdmin):
  list_display = (
    '__str__',
    'account_name',
    'n_nota',
    'market',
    'date',
    'total_mov',
    'total_liq',
    'tx_bovespa',
    'tx_liquida',
    'tx_registro',
    'corretagem',
    'outros',
    'pdf',
    'last_update',
  )
  search_fields = ('account_name',)
  list_filter = ('date',)
