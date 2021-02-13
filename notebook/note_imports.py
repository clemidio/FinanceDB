import os


#  Desabilitar a sincronização no contexto assíncrono do django
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"

