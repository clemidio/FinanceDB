from django.urls import path
from . import views as v

app_name = 'transaction'


urlpatterns = [

    path('list/', v.list_transactions,
         name='url_list_transactions'),
    path('new/', v.Create_transaction.as_view(),
         name='url_new_transaction'),
    path('update/<int:pk>/',
         v.Update_transaction.as_view(), name='url_update_transaction'),
    path('detail/<int:pk>/',
         v.detail_transaction, name='url_detail_transaction'),
    path('delete/<int:pk>/',
         v.delete_transaction, name='url_delete_transaction'),

    path('test/', v.test, name='url_test'),
    path('serverside/', v.transactions_serverside,
         name='url_transactions_serverside'),
    path('json/', v.transactions_json,
         name='url_transactions_json'),


]
