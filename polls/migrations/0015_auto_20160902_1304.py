# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-02 11:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0014_auto_20160902_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='produit_titre',
            field=models.CharField(default=b'', max_length=100),
        ),
    ]
