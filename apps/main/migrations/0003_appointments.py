# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-20 18:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20161220_1029'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointDay', models.IntegerField()),
                ('appointTime', models.IntegerField()),
                ('tasks', models.CharField(max_length=100)),
            ],
        ),
    ]
