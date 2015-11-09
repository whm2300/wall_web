# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('email', models.CharField(max_length=200, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=64)),
                ('create_date', models.DateTimeField(verbose_name=b'date created')),
                ('delegate_ip', models.CharField(max_length=64, null=True)),
                ('delegate_port', models.IntegerField(default=0)),
            ],
        ),
    ]
