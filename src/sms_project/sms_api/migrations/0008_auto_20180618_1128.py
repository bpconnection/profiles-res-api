# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-18 17:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms_api', '0007_auto_20180618_1052'),
    ]

    operations = [
        migrations.RenameField(
            model_name='envio_contenido',
            old_name='id_contenido_programado',
            new_name='contenido_programado',
        ),
    ]