from django.urls import path
from . import views as v

app_name = 'core'


urlpatterns = [

    path('', v.home, name='home'),

    path('time/', v.current_datetime),
    path('upload_file/', v.upload_file, name='url_upload_file'),

]
