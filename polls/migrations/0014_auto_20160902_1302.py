# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-02 11:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0013_auto_20160902_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='produit_description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='produit',
            name='produit_text',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='produit',
            name='produit_titre',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
