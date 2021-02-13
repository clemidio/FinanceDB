import math
from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from django.http import Http404
from django.core.files.storage import FileSystemStorage
from .form import AssetForm
from .models import Asset

# Create your views here.


def list_assets(request):
    # data['transactions'] = Transaction.objects.all()
    assets = Asset.objects.all()
    search = request.GET.get('search')
    if search:
        assets = Asset.objects.filter(name__icontains=search)
    return render(request, 'list_assets.html', {'objects': assets})


def detail_asset(request, pk):
    try:
        asset = Asset.objects.get(pk=pk)
    except Asset.DoesNotExist:
        raise Http404('asset does not exist')
    return render(request, 'detail_asset.html', {'object': asset})


def new_asset(request):
    form = AssetForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('url_list_assets')
    else:
        print("Deu errado")
    return render(request, 'new_asset.html', {'form': form})


def update_asset(request, pk):
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
    return render(request, 'new_asset.html', {'form': form, 'asset': asset})


def delete_asset(request, pk):
    try:
        asset = Asset.objects.get(pk=pk)
    except Asset.DoesNotExist:
        raise Http404('asset does not exist')
    asset.delete()
    return redirect('url_list_assets')


def assets_json1(request):
    assets = Asset.objects.all()
    data = [asset.to_dict_json() for asset in assets]
    return JsonResponse({'data': data})


def assets_json(request):
    assets = Asset.objects.all()
    total = assets.count()

    _start = request.GET.get('start')
    _length = request.GET.get('length')
    if _start and _length:
        start = int(_start)
        length = int(_length)
        page = math.ceil(start / length) + 1  # [opcional]
        per_page = length  # [opcional]

        assets = assets[start:start + length]

    data = [asset.to_dict_json() for asset in assets]
    response = {
        'data': data,
        # 'page': page,  # [opcional]
        # 'per_page': per_page,  # [opcional]
        'recordsTotal': total,
        'recordsFiltered': total,
    }
    return JsonResponse(response)


def assets_serverside(request):
    template_name = 'assets_serverside.html'
    return render(request, template_name)
