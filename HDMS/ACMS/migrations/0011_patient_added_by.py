# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-22 15:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ACMS', '0010_auto_20160822_1542'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='added_by',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
