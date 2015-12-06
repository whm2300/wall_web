# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_manage', '0009_ipportpassword'),
    ]

    operations = [
        migrations.AddField(
            model_name='ipportpassword',
            name='email',
            field=models.CharField(default=b'nouser', max_length=200),
        ),
    ]
