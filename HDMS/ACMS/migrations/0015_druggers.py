# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-25 19:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ACMS', '0014_merge'),
    ]

    operations = [
        migrations.CreateModel(
            name='druggers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drug_name', models.CharField(max_length=50)),
                ('drug_code', models.CharField(max_length=15)),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('added_by', models.ForeignKey(default=7, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
