# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-07 11:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0023_luser'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='lusers',
            field=models.ManyToManyField(to='users.Luser'),
        ),
    ]
