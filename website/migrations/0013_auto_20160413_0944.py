# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-13 09:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0012_blogpost_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='text',
            field=models.TextField(verbose_name=b'text'),
        ),
    ]
