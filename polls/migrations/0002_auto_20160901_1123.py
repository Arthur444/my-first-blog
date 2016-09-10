# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-01 09:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to=b'photos/')),
            ],
        ),
        migrations.CreateModel(
            name='produit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('produit_titre', models.CharField(default=b'', max_length=100)),
                ('produit_description', models.TextField(default=b'')),
                ('produit_text', models.TextField(default=b'')),
                ('pub_date', models.DateTimeField(default=datetime.datetime.now, verbose_name=b'date published')),
                ('photo', models.ImageField(default=b'', upload_to=b'photos/')),
                ('produit_video', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='projectBuildTests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.CharField(default=b'', max_length=50)),
                ('build', models.CharField(default=b'', max_length=10)),
                ('testName', models.CharField(default=b'', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slide_titre', models.CharField(default=b'', max_length=100)),
                ('pub_date', models.DateTimeField(default=datetime.datetime.now, verbose_name=b'date published')),
                ('photo', models.ImageField(default=b'', upload_to=b'diapo/')),
            ],
        ),
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.AddField(
            model_name='image',
            name='produit',
            field=models.ForeignKey(default=b'', on_delete=django.db.models.deletion.CASCADE, to='polls.produit'),
        ),
    ]