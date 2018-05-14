# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-04-20 09:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0034_add_allow_block_domain_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='challengephase',
            name='max_concurrent_submissions_allowed',
            field=models.PositiveIntegerField(default=3),
        ),
    ]
