# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-20 19:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_appointments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointments',
            name='appointDay',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='appointments',
            name='appointTime',
            field=models.CharField(max_length=100),
        ),
    ]
