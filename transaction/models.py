from django.db import models
from django.urls import reverse_lazy
from asset.models import Asset
from nota.models import Nota
from core.models import TimeStampedModel

OPERATION_TYPE = (
    ('C', 'Compra'),
    ('V', 'Venda'),
    ('DT', 'Day Trade'),
    ('S/I', 'Split ou Inplit'),
    ('AT', 'Alteração Ticker'),
    ('BN', 'Bonificação'),
    ('AM', 'Amortização'),
    ('SUB', 'Compra de Subscrição'),
    ('V.SUB', 'Venda Direito Subscrição'),
    ('V.SOB', 'Venda de sobras de S/I ou Cisão'),
    ('CISÃO', 'Operação de cião de capital social'),
    ('EX.OPC', 'Venda ou Compra por Exercício de Opção'),
)

# Create your models here.


class Transaction(TimeStampedModel):
    """A model of a Transactions."""
    # id = models.IntegerField(primary_key=True) #models.AutoField(primary_key=True)
    asset = models.ForeignKey(
        Asset, related_name='asset', on_delete=models.CASCADE)
    date = models.DateField()
    operation = models.CharField(
        max_length=6, choices=OPERATION_TYPE, default='C')
    amount = models.DecimalField(
        max_digits=10, decimal_places=5, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=5)
    commission = models.DecimalField(
        max_digits=10, decimal_places=5, null=True, blank=True)
    nota_id = models.ForeignKey(
        Nota, related_name='nota', on_delete=models.CASCADE)
    account_bank = models.CharField(max_length=45, null=True, blank=True)
    obs = models.CharField(max_length=200, null=True, blank=True)
    total = models.DecimalField(
        max_digits=10, decimal_places=5, null=True, blank=True)
    profit = models.DecimalField(
        max_digits=10, decimal_places=5, null=True, blank=True)
    last_update = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date',)
        verbose_name = 'transaction'
        verbose_name_plural = 'transactions'

    def get_absolute_url(self):
        # retorna a url no formato /bands/1/
        return reverse_lazy('url_detail_transaction', kwargs={'pk': self.pk})

    def __str__(self):
        return str(self.pk)

    def to_dict_json(self):
        data = {
            'id': self.id,
            'asset': self.asset.sigla,
            'date': self.date,
            'operation': self.operation,
            'amount': self.amount,
            'price': self.price,
            'nota_id': self.nota_id.id,
            'account_bank': self.account_bank,
        }
        return data
