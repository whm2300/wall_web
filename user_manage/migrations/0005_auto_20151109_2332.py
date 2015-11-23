# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('user_manage', '0004_auto_20151109_2328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 9, 15, 32, 15, 305244, tzinfo=utc), verbose_name=b'date created'),
        ),
    ]
