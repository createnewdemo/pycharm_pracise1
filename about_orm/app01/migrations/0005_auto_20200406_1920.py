# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-04-06 11:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0004_auto_20200406_1620'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.DecimalField(decimal_places=2, default=100, max_digits=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='author',
            name='books',
            field=models.ManyToManyField(related_name='authors', to='app01.Book'),
        ),
    ]