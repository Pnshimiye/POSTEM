# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-03 12:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20190403_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]