# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-13 03:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rate', '0002_auto_20170413_0518'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Commenter',
            new_name='Student',
        ),
        migrations.AddField(
            model_name='assessment',
            name='difficulty_grade',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='assessment',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='rate.Student'),
        ),
    ]
