# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-04-11 03:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=32)),
                ('position', models.CharField(max_length=32)),
                ('company', models.CharField(choices=[('1', '黄土高坡总公司'), ('2', '家里蹲分公司'), ('3', '德玛西亚分公司')], max_length=32)),
                ('phone', models.CharField(max_length=32)),
                ('last_time', models.DateTimeField(blank=True, null=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
