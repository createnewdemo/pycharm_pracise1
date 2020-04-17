# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-04-06 08:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_auto_20200406_1514'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='姓名')),
            ],
        ),
        migrations.AlterField(
            model_name='book',
            name='pub',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', related_query_name='book', to='app01.Publisher'),
        ),
        migrations.AddField(
            model_name='author',
            name='books',
            field=models.ManyToManyField(to='app01.Book'),
        ),
    ]
