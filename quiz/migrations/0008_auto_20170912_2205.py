# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-12 22:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0007_apirequestcount_last_requested_on'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apirequestcount',
            name='id',
        ),
        migrations.AlterField(
            model_name='apirequestcount',
            name='date',
            field=models.DateField(primary_key=True, serialize=False),
        ),
    ]
