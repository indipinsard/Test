# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-29 18:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courbe_de_charge', '0003_remove_userslp_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='userslp',
            name='user',
            field=models.CharField(default='blabla', max_length=50),
        ),
    ]
