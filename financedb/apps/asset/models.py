from django.db import models
from django.urls import reverse_lazy

# Create your models here.


class Asset(models.Model):
    """A model of a asset."""
    sigla = models.CharField(max_length=45, unique=True, primary_key=True)
    symbol = models.CharField(max_length=45, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    isin = models.CharField(max_length=45, null=True, blank=True)
    classe = models.CharField(max_length=45, null=True, blank=True)
    market_cod = models.CharField(max_length=45, null=True, blank=True)
    market = models.CharField(max_length=45, null=True, blank=True)
    price = models.DecimalField(
        max_digits=10, decimal_places=5, null=True, blank=True)
    setor = models.CharField(max_length=45, null=True, blank=True)
    subsetor = models.CharField(max_length=45, null=True, blank=True)
    segmento = models.CharField(max_length=45, null=True, blank=True)
    codcvm = models.CharField(max_length=15, null=True, blank=True)
    cnpj = models.CharField(max_length=45, null=True, blank=True)
    razao_social = models.CharField(max_length=100, null=True, blank=True)
    cnpj_adm = models.CharField(max_length=45, null=True, blank=True)
    razao_social_adm = models.CharField(max_length=100, null=True, blank=True)
    last_update = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('sigla',)
        verbose_name = 'Asset'
        verbose_name_plural = 'Assets'

    def __str__(self):
        return self.sigla

    def get_absolute_url(self):
        # retorna a url no formato /bands/1/
        return reverse_lazy('asset:url_asset_detail', kwargs={'pk': self.sigla})

    def get_members_count(self):
        # count members by band
        # conta os membros por banda
        return self.asset.count()

    def to_dict_json(self):
        data = {
            'sigla': self.sigla,
            'name': self.name,
            'price': self.price,
            'classe': self.classe,
            'setor': self.setor,
            'subsetor': self.subsetor,
            'segmento': self.segmento,
        }
        return data
