# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-24 23:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wishlist_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='updated_at',
            field=models.DateField(auto_now=True),
        ),
    ]
