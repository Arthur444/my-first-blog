# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-02 10:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_auto_20160902_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='produit_video',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
