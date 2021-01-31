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
from django.urls import path
from core import views as v
# from transactions.views import current_datetime
# from transactions.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('time/', v.current_datetime),    
    path('assets/', v.show_assets, name='url_list_assets'),
    path('update_asset/<int:pk>/', v.update_asset, name='url_update_asset'),
    path('delete_asset/<int:pk>/', v.delete_asset, name='url_delete_asset'),
    path('new_asset/', v.new_asset, name='url_new_asset'),
    path('assets_json/', v.assets_json, name='url_assets_json'),
    path('', v.home, name='home'),
]
