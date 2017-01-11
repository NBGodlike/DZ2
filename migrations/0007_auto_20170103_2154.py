# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-03 18:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_subscription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='Duration',
            field=models.TextField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='Name',
            field=models.TextField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='Picture',
            field=models.ImageField(null=True, upload_to=b'css/'),
        ),
        migrations.AlterField(
            model_name='course',
            name='Teacher',
            field=models.TextField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='Value',
            field=models.TextField(max_length=255, null=True),
        ),
    ]