# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-07 11:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0024_course_lusers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='users',
        ),
    ]