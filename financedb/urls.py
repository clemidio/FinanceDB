"""financedb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from core import views as vw_c
from asset import views as vw_a
from transaction import views as vw_t
from portfolio import views as vw_p
# from nota import views as vw_n
# from transactions.views import current_datetime
# from transactions.views import home

urlpatterns = [
    path('', vw_c.home, name='home'),
    path('admin/', admin.site.urls),

    path('time/', vw_c.current_datetime),
    path('upload_file/', vw_c.upload_file, name='url_upload_file'),

    # path('portfolio/', include('portfolio.urls')),

    path('portfolio/list', vw_p.list_portfolio, name='url_list_portfolio'),

    path('list_transactions/', vw_t.list_transactions,
         name='url_list_transactions'),
    path('new_transaction/', vw_t.Create_transaction.as_view(),
         name='url_new_transaction'),
    path('update_transaction/<int:pk>/',
         vw_t.Update_transaction.as_view(), name='url_update_transaction'),
    path('detail_transaction/<int:pk>/',
         vw_t.detail_transaction, name='url_detail_transaction'),
    path('delete_transaction/<int:pk>/',
         vw_t.delete_transaction, name='url_delete_transaction'),

    path('test/', vw_t.test, name='url_test'),
    path('transaction/serverside/', vw_t.transactions_serverside,
         name='url_transactions_serverside'),
    path('transaction/json/', vw_t.transactions_json,
         name='url_transactions_json'),

    path('asset/serverside/', vw_a.assets_serverside,
         name='url_assets_serverside'),
    path('list_assets/', vw_a.list_assets, name='url_list_assets'),
    path('detail_asset/<str:pk>/', vw_a.detail_asset, name='url_asset_detail'),
    path('update_asset/<str:pk>/', vw_a.update_asset, name='url_update_asset'),
    path('delete_asset/<str:pk>/', vw_a.delete_asset, name='url_delete_asset'),
    path('new_asset/', vw_a.new_asset, name='url_new_asset'),
    path('asset/json/', vw_a.assets_json, name='url_assets_json'),

]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
