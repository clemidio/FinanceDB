from django.db import models
# from asset.models import Asset
# from nota.models import Nota

# # Create your models here.
# # Transform tabela em view no database


# class Portfolio(models.Model):
#     """A model of a Transactions."""
#     # id = models.IntegerField(primary_key=True) #models.AutoField(primary_key=True)
#     asset = models.ForeignKey(
#         Asset, related_name='asset', on_delete=models.CASCADE)
#     position = models.DecimalField(
#         max_digits=10, decimal_places=5, null=True, blank=True, default=0)
#     avg_price = models.DecimalField(max_digits=10, decimal_places=5)
#     cost_basic = models.DecimalField(max_digits=10, decimal_places=5)
#     mkt_value = models.DecimalField(max_digits=10, decimal_places=5)
#     profit = models.DecimalField(max_digits=10, decimal_places=5)
#     percent = models.DecimalField(max_digits=10, decimal_places=5)
#     last_update = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         ordering = ('mkt_value',)
#         verbose_name = 'portifolio'

#     # def __str__(self):
#     #     return self.id
#     def __str__(self):
#         return '{} - {}'.format(self.pk, self.asset)
