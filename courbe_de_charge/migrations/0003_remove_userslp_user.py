# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-29 18:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courbe_de_charge', '0002_userslp_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userslp',
            name='user',
        ),
    ]
