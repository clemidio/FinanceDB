from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime
from .form import AssetForm
from .models import Asset
from .models import Transaction

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def show_assets(request):
    data = {}    
    data['transactions'] = Transaction.objects.all()
    data['assets'] = Asset.objects.all()
    return render(request, 'core/assets.html',data)

def new_asset(request):
    data = {}    
    form = AssetForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('url_list_assets')
    else:
        print("Deu errado")
    data['form'] = form
    return render(request, 'core/new_asset.html',data)

def update_asset(request,pk):
    data = {}  
    try:
        asset = Asset.objects.get(pk=pk)
    except Asset.DoesNotExist:
        raise Http404('asset does not exist')
    
    form = AssetForm(request.POST or None, instance=asset)
    if form.is_valid():
        form.save()
        return redirect('url_list_assets')
    else:
        print("Deu errado")
    data['form'] = form
    data['asset'] = asset
    return render(request, 'core/new_asset.html',data)

def delete_asset(request,pk):
    try:
        asset = Asset.objects.get(pk=pk)
    except Asset.DoesNotExist:
        raise Http404('asset does not exist')
    asset.delete()
    return redirect('url_list_assets')

def home(request):
    data = {}
    data['now'] = datetime.datetime.now()
    return render(request, 'core/home.html',data)