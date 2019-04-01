# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-01 21:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='content',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='project',
            name='design',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='project',
            name='usability',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
