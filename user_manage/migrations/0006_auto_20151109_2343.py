# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('user_manage', '0005_auto_20151109_2332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 9, 15, 43, 9, 789752, tzinfo=utc), verbose_name=b'date created'),
        ),
    ]
