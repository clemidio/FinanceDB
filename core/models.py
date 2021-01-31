from django.db import models
from django.urls import reverse_lazy

class Asset(models.Model):
    """A model of a asset."""
    sigla = models.CharField(max_length=45)
    symbol = models.CharField(max_length=45,null=True, blank=True)
    name = models.CharField(max_length=200,null=True, blank=True)
    isin = models.CharField(max_length=45,null=True, blank=True)
    classe = models.CharField(max_length=45,null=True, blank=True)
    market_cod = models.CharField(max_length=45,null=True, blank=True)
    market = models.CharField(max_length=45,null=True, blank=True)
    price = models.DecimalField(max_digits=10,decimal_places=5,null=True, blank=True)
    setor = models.CharField(max_length=45,null=True, blank=True)
    subsetor = models.CharField(max_length=45,null=True, blank=True)
    segmento = models.CharField(max_length=45,null=True, blank=True)
    codcvm = models.CharField(max_length=15,null=True, blank=True)
    cnpj = models.CharField(max_length=45,null=True, blank=True)
    razao_social = models.CharField(max_length=100,null=True, blank=True)
    cnpj_adm = models.CharField(max_length=45,null=True, blank=True)
    razao_social_adm = models.CharField(max_length=100,null=True, blank=True)
    last_update = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('sigla',)
        verbose_name = 'Asset'
        verbose_name_plural = 'Assets'

    def __str__(self):
        return self.sigla

    def get_absolute_url(self):
        # retorna a url no formato /bands/1/
        return reverse_lazy('asset_detail', kwargs={'pk': self.pk})

    def get_members_count(self):
        # count members by band
        # conta os membros por banda
        return self.asset.count()
    
    def to_dict_json(self):
        data = {
            'id':self.id,
            'sigla': self.sigla,
            'name': self.name,
            'price': self.price,
            'setor': self.setor,
        }
        return data



class Transaction(models.Model):
    """A model of a Transactions."""
    id = models.IntegerField(primary_key=True) #models.AutoField(primary_key=True)
    date = models.DateField() 
    amont = models.DecimalField(max_digits=10,decimal_places=5,null=True, blank=True)
    price = models.DecimalField(max_digits=10,decimal_places=5)
    commission = models.DecimalField(max_digits=10,decimal_places=5,null=True, blank=True)
    nota_id = models.CharField(max_length=15,null=True, blank=True)
    asset = models.ForeignKey("Asset", related_name='asset', on_delete=models.CASCADE)
    obs = models.CharField(max_length=200,null=True, blank=True)
    last_update = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date',)
        verbose_name = 'transaction'
        verbose_name_plural = 'transactions'

    # def __str__(self):
    #     return self.id
    def __str__(self):
        if self.id==None:
            return "ERROR-CUSTOMER NAME IS NULL"
        return str(self.id)

# Create your models here.
