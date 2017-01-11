# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-04 17:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20170104_1302'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='courses',
            field=models.ManyToManyField(related_name='users', to='users.Course'),
        ),
        migrations.AlterField(
            model_name='course',
            name='Picture',
            field=models.ImageField(null=True, upload_to=b'css2/'),
        ),
    ]