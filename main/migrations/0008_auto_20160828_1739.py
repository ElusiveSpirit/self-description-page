# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-28 17:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20160825_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
