import math
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.generic import CreateView, UpdateView, ListView
from django.http import Http404
from .form import TransactionForm
from .models import Transaction
from .models import Asset

# Create your views here.


def test(request):
    # data['transactions'] = Transaction.objects.all()
    transactions = Transaction.objects.all()[:50]
    return render(request, 'index.html', {'objects': transactions})


def list_transactions(request):
    # data['transactions'] = Transaction.objects.all()
    transactions = Transaction.objects.all()
    return render(request, 'list_transactions.html', {'objects': transactions})


def detail_transaction(request, pk):
    try:
        transaction = Transaction.objects.get(pk=pk)
    except Transaction.DoesNotExist:
        raise Http404('asset does not exist')
    return render(request, 'detail_transaction.html', {'object': transaction})


class Create_transaction(CreateView):
    model = Transaction
    template_name = 'new_transaction.html'
    form_class = TransactionForm


class Update_transaction(UpdateView):
    model = Transaction
    template_name = 'new_transaction.html'
    form_class = TransactionForm


def delete_transaction(request, pk):
    try:
        transaction = Transaction.objects.get(pk=pk)
    except Transaction.DoesNotExist:
        raise Http404('asset does not exist')
    transaction.delete()
    return redirect('url_list_assets')


def transactions_json(request):
    transactions = Transaction.objects.all()
    total = transactions.count()

    _start = request.GET.get('start')
    _length = request.GET.get('length')
    if _start and _length:
        start = int(_start)
        length = int(_length)
        page = math.ceil(start / length) + 1  # [opcional]
        per_page = length  # [opcional]

        transactions = transactions[start:start + length]

    data = [transaction.to_dict_json() for transaction in transactions]
    response = {
        'data': data,
        # 'page': page,  # [opcional]
        # 'per_page': per_page,  # [opcional]
        'recordsTotal': total,
        'recordsFiltered': total,
    }
    return JsonResponse(response)


def transactions_serverside(request):
    template_name = 'transactions_serverside.html'
    return render(request, template_name)
