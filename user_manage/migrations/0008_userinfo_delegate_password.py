# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_manage', '0007_auto_20151110_2125'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='delegate_password',
            field=models.CharField(max_length=128, null=True),
        ),
    ]
