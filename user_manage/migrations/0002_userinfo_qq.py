# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_manage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='qq',
            field=models.CharField(default=123456, max_length=32),
            preserve_default=False,
        ),
    ]
