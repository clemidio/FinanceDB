from django.contrib import admin
from .models import Asset

# Register your models here.
#admin.site.register(Asset)
@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
  list_display = (
    '__str__',
    'sigla',
    'symbol',
    'name',
    'isin',
    'classe',
    'market_cod',
    'market',
    'price',
    'setor',
    'subsetor',
    'segmento',
    'codcvm',
    'cnpj',
    'razao_social',
    'cnpj_adm',
    'razao_social_adm',
    'last_update',

  )
  search_fields = ('sigla',)
  list_filter = ('subsetor',)