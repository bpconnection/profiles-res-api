# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-20 18:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms_api', '0015_auto_20180620_1132'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='club',
            name='plataforma_envio',
        ),
        migrations.DeleteModel(
            name='Plataforma_envio',
        ),
    ]
