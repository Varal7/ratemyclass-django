# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-21 19:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rate', '0006_auto_20170413_0610'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='first_name',
            field=models.CharField(default='Toto', max_length=254, verbose_name='prénom'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='last_name',
            field=models.CharField(default='Dutot', max_length=254, verbose_name='nom de famille'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='course',
            name='code',
            field=models.CharField(max_length=32, verbose_name='code'),
        ),
    ]
