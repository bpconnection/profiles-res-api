# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-20 16:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sms_api', '0012_configuracion_conexion_tigohn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configuracion_conexion_tigohn',
            name='dlr_mask',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='configuracion_conexion_tigohn',
            name='dlr_url',
            field=models.CharField(max_length=200),
        ),
    ]