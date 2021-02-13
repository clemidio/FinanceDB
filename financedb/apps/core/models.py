from django.db import models
# from django.urls import reverse_lazy


class TimeStampedModel(models.Model):
    created = models.DateTimeField(
        'criado em',
        auto_now_add=True, auto_now=False
    )
    modified = models.DateTimeField(
        'modificado em',
        auto_now_add=False, auto_now=True
    )

    class Meta:
        abstract = True

# Create your models here.
