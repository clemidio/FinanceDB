from django.urls import path
from . import views as v

app_name = 'asset'


urlpatterns = [

    path('serverside/', v.assets_serverside,
         name='url_assets_serverside'),
    path('list/', v.list_assets, name='url_list_assets'),
    path('detail/<str:pk>/', v.detail_asset, name='url_asset_detail'),
    path('update/<str:pk>/', v.update_asset, name='url_update_asset'),
    path('delete/<str:pk>/', v.delete_asset, name='url_delete_asset'),
    path('new/', v.new_asset, name='url_new_asset'),
    path('json/', v.assets_json, name='url_assets_json'),

]
