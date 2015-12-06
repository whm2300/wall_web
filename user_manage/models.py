import datetime

from django.db import models
from django.utils import timezone

class UserInfo(models.Model):
    def __unicode__(self):
        return self.email

    email = models.CharField(max_length = 200, primary_key = True)
    name = models.CharField(max_length = 32)
    qq = models.CharField(max_length = 32)
    password = models.CharField(max_length = 64)
    create_date = models.DateTimeField('date created', default = timezone.now)
    delegate_ip = models.CharField(max_length = 64, null = True)
    delegate_port = models.IntegerField(default = 0)
    delegate_password = models.CharField(max_length = 128, null = True)

class IpPortPassword(models.Model):
    def __unicode__(self):
        return str(self.port)

    ip = models.CharField(max_length = 32)
    port = models.IntegerField(primary_key = True)
    password = models.CharField(max_length = 64)
    encryption = models.CharField(max_length = 16)
    email = models.CharField(max_length = 200, default = 'nouser')
