from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
import datetime


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


def upload_file(request):
    url = []
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        url = fs.url(name)
        print(url)
    return render(request, 'core/upload_file.html', {'url': url})  #


def home(request):
    return render(request, 'core/home.html', {'now': datetime.datetime.now()})
