# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-03 09:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20190401_2349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='prof_pic',
            field=models.ImageField(upload_to='profile/'),
        ),
    ]