# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-31 22:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ACMS', '0002_auto_20160731_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hmo_list',
            name='mobile',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
