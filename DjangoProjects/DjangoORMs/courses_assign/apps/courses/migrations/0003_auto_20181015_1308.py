# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-10-15 20:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20181015_1304'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='description',
            name='id',
        ),
        migrations.AlterField(
            model_name='description',
            name='course',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='description', serialize=False, to='courses.Course'),
        ),
    ]
