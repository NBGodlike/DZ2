# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-02 13:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_course_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(null=True)),
                ('course_id', models.IntegerField(null=True)),
            ],
        ),
    ]
