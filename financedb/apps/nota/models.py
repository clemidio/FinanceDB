from django.db import models

# Create your models here.


class Nota(models.Model):
    """A model of a Nota."""
    # id = models.IntegerField(primary_key=True) #models.AutoField(primary_key=True)
    account_name = models.CharField(max_length=45)
    n_nota = models.CharField(max_length=45)
    market = models.CharField(max_length=45, null=True, blank=True)
    date = models.DateField()
    total_mov = models.DecimalField(
        max_digits=10, decimal_places=5, null=True, blank=True)
    total_liq = models.DecimalField(
        max_digits=10, decimal_places=5, null=True, blank=True)
    tx_bovespa = models.DecimalField(
        max_digits=10, decimal_places=5, null=True, blank=True)
    tx_liquida = models.DecimalField(
        max_digits=10, decimal_places=5, null=True, blank=True)
    tx_registro = models.DecimalField(
        max_digits=10, decimal_places=5, null=True, blank=True)
    corretagem = models.DecimalField(
        max_digits=10, decimal_places=5, null=True, blank=True)
    outros = models.DecimalField(
        max_digits=10, decimal_places=5, null=True, blank=True)
    pdf = models.FileField(upload_to='uploads/notas/', null=True, blank=True)
    last_update = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date',)
        verbose_name = 'nota'
        verbose_name_plural = 'notas'

    def __str__(self):
        if self.id == None:
            return "ERROR-CUSTOMER NAME IS NULL"
        return str(self.id)
