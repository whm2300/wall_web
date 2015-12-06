# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_manage', '0008_userinfo_delegate_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='IpPortPassword',
            fields=[
                ('ip', models.CharField(max_length=32)),
                ('port', models.IntegerField(serialize=False, primary_key=True)),
                ('password', models.CharField(max_length=64)),
                ('encryption', models.CharField(max_length=16)),
            ],
        ),
    ]
