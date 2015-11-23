# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user_manage', '0006_auto_20151109_2343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='create_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'date created'),
        ),
    ]
