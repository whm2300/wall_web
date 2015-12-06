from django.contrib import admin

from .models import UserInfo
from .models import IpPortPassword 

admin.site.register(UserInfo)
admin.site.register(IpPortPassword)
