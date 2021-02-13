from django.shortcuts import render
from transaction.models import Transaction
from asset.models import Asset
from django.db.models import Count, Sum, Avg

# Create your views here.


def list_portfolio(request):
    # data['transactions'] = Transaction.objects.all()
    # portfolio = Transaction.objects.all()
    data = []
    objects = []
    asset = Asset.objects.all()
    transactions = Transaction.objects.order_by('asset').values(
        'asset').annotate(Sum('amount'), Avg('price'))
    for pos in transactions:
        if pos['amount__sum'] > 0:
            data = dict(
                asset=pos['asset'],
                position="{:.2f}".format(pos['amount__sum']),
                avg_price="{:.2f}".format(pos['price__avg']),
                cost_basic=0,
                mkt_value=0,
                profit=0,
                percent=0,
            )
            objects.append(data)

    return render(request, 'list_portfolio.html', {'objects': objects, 'asset': asset})
