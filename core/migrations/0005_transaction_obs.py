# Generated by Django 3.1.5 on 2021-01-29 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20210129_1330'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='obs',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
